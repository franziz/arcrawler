from lib.config.factory import ConfigFactory
import os
import zipfile
import requests

def zipdir(path, ziph):    
	for root, dirs, files in os.walk(path):
		for file in files:			
			ziph.write(os.path.join(root, file))

if __name__ == '__main__':
    print("[deploy][debug] Zipping build folder...")
    zipf = zipfile.ZipFile('build.zip', 'w', zipfile.ZIP_DEFLATED)
    os.chdir(os.path.join(".","build"))
    zipdir(".", zipf)
    zipf.close()
    os.chdir(os.path.join(".."))

    print("[deploy][debug] Reading config...")
    route_config = ConfigFactory.get(ConfigFactory.ROUTE)
    cd_server    = route_config.get("cd_server")

    print("[deploy][debug] Sending the zip...")
    url  = "http://%s:%s/deploy?route=%s" % (cd_server["ip"], cd_server["port"], cd_server["route"])
    file = {"file":open("build.zip", "rb")}
    requests.post(url,files=file)

    print("[deploy][debug] Deleting the zip...")
    os.remove("build.zip")