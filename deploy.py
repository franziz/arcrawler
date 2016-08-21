from lib.shell          import Shell
from lib.config.factory import ConfigFactory
from curtsies           import fmtstr
import subprocess
import os

if __name__ == "__main__":
	try:
		route_config = ConfigFactory.get(ConfigFactory.ROUTE)

		# This method will deploy the source file.
		# Deploying changes for engine is a complicated way and cannot be done in a short time
		os.chdir("/root/app/src")
		Shell.run_command("git checkout %s" % route_config.get("source")["branch"])
		Shell.run_command("git add --all .")
		Shell.run_command(["git", "commit", "-m" ,"'Automated commit from deploy.py'"])
		Shell.run_command("git push")
		print(fmtstr("[deploy][success] Success!", "green"))
	except CommandError as command_error:
		print(fmtstr("[deploy][error] %s" % command_error, "red"))