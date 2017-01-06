import os
import sys

TEST_DIR   = os.path.abspath(os.path.dirname(__file__))
PARENT_DIR = os.path.join(TEST_DIR, '..')
sys.path.insert(0, PARENT_DIR)

from lib.builder  import Builder
from lib.deployer import Deployer
import json
import click
import time

@click.command()
@click.option("--config", default=os.path.join(os.getcwd(),"config","batch_build.json"), prompt="Config file")
def run(config):
	file   = open(config)
	config = file.read()
	config = json.loads(config)

	selected_sections = []
	config_sections   = config["sections"]
	sections 		  = Builder.get_sections()
	for config_section in config_sections:
		selected_section = [section for section in sections if section.name == config_section]
		selected_sections.extend(selected_section)
		if len(selected_section) == 0:
			print("Not found %s" % (config_section))
	
	assert len(config_sections) == len(selected_sections), "Cannot find one or some sections inside your config"
	deployer        = Deployer()
	failed_sections = []
	for selected_section in selected_sections:
		try:
			click.echo("Building %s" % selected_section.name)
			Builder.build(selected_section, log_callback)
			deployer.deploy()
		except OSError:
			click.echo("OSError!")
			failed_sections.append(selected_section.name)
		time.sleep(1)
	for section in failed_sections:
		click.echo(section)

def log_callback(message):
	click.echo(message)


if __name__ == "__main__":
	run()