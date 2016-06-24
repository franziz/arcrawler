# -*- coding: utf-8 -*-
"""
All code involving requests and responses over the http network
must be abstracted in this file.
"""
__title__ = 'newspaper'
__author__ = 'Lucas Ou-Yang'
__license__ = 'MIT'
__copyright__ = 'Copyright 2014, Lucas Ou-Yang'

import logging
import requests
import socket

from .configuration    import Configuration
from .mthreading       import ThreadPool
from .settings         import cj
from ...proxy_switcher import ProxySwitcher

log = logging.getLogger(__name__)


def get_request_kwargs(timeout, useragent):
    """This Wrapper method exists b/c some values in req_kwargs dict
    are methods which need to be called every time we make a request
    """
    return {
        'headers': {'User-Agent': useragent},
        'cookies': cj(),
        'timeout': timeout,
        'allow_redirects': True
    }


def get_html(url, config=None, response=None):
    """Retrieves the html for either a url or a response object. All html
    extractions MUST come from this method due to some intricies in the
    requests module. To get the encoding, requests only uses the HTTP header
    encoding declaration requests.utils.get_encoding_from_headers() and reverts
    to ISO-8859-1 if it doesn't find one. This results in incorrect character
    encoding in a lot of cases.
    """
    FAIL_ENCODING = 'ISO-8859-1'
    config = config or Configuration()
    useragent = config.browser_user_agent
    timeout = config.request_timeout

    if response is not None:
        if response.encoding != FAIL_ENCODING:
            return response.text
        return response.content

    proxy_is_ok = False
    while not proxy_is_ok:
        try:
            print("[newspaper] Getting HTML")
            html = None

            switcher = ProxySwitcher()
            response = requests.get(
                url=url,
                proxies=switcher.get_proxy(),
                **get_request_kwargs(timeout, useragent)
            )
            status_code = response.status_code

            html = response.text if response.encoding != FAIL_ENCODING else response.content
            if config.http_success_only: 
                print("[newspaper] Error: {}".format(response.status_code))
                response.raise_for_status()  # fail if other than "ok" response
            proxy_is_ok = True
        except requests.exceptions.ProxyError as proxy_error:
            log.debug('%s on %s' % (proxy_error, url))
            print("[newspaper] Ops! Proxy is not working. Try again...")
            proxy_is_ok = False
        except socket.timeout as rto:
            log.debug('%s on %s' % (rto, url))
            print("[newspaper] Ops! Request Time Out")
            proxy_is_ok = False
        except requests.exceptions.RequestException as e:
            log.debug('%s on %s' % (e, url))
            print("[newspaper] Ops! Something wrong. Try again...")
            proxy_is_ok = False
        #end try
    #end while
    html = '' if html is None else html
    return html
#end def

class MRequest(object):
    """Wrapper for request object for multithreading. If the domain we are
    crawling is under heavy load, the self.resp will be left as None.
    If this is the case, we still want to report the url which has failed
    so (perhaps) we can try again later.
    """
    def __init__(self, url, config=None):
        self.url = url
        self.config = config
        config = config or Configuration()
        self.useragent = config.browser_user_agent
        self.timeout = config.request_timeout
        self.resp = None

    def send(self):
        try:
            self.resp = requests.get(self.url, **get_request_kwargs(
                                     self.timeout, self.useragent))
            if self.config.http_success_only:
                self.resp.raise_for_status()
        except requests.exceptions.RequestException as e:
            log.critical('[REQUEST FAILED] ' + str(e))
    #end def
#end class


def multithread_request(urls, config=None):
    """Request multiple urls via mthreading, order of urls & requests is stable
    returns same requests but with response variables filled.
    """
    config = config or Configuration()
    num_threads = config.number_threads
    timeout = config.thread_timeout_seconds

    pool = ThreadPool(num_threads, timeout)

    m_requests = []
    for url in urls:
        m_requests.append(MRequest(url, config))

    for req in m_requests:
        pool.add_task(req.send)

    pool.wait_completion()
    return m_requests
#end def