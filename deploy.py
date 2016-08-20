from lib.exceptions     import CommandError
from lib.config.factory import ConfigFactory
from curtsies           import fmtstr
import subprocess
import os

def run_command(command=None):
	assert command is not None, "command is not defined."
	command = command.split(" ") if not type(command) is list else command
	proc    = subprocess.Popen(command, stdout=subprocess.PIPE)
	success = False
	for line in proc.stdout:
		line = line.decode("utf-8")
		if "nothing to commit" in line:
			success = True
	proc.wait()

	exit_code = proc.returncode
	if exit_code != 0 and not success: raise CommandError("Exit: %s" % exit_code)
	return proc.returncode

if __name__ == "__main__":
	try:
		route_config = ConfigFactory.get(ConfigFactory.ROUTE)

		# This method will deploy the source file.
		# Deploying changes for engine is a complicated way and cannot be done in a short time
		os.chdir("/root/app/src")
		run_command("git checkout %s" % route_config.get("source")["branch"])
		run_command("git add --all .")
		run_command(["git", "commit", "-m" ,"'Automated commit from deploy.py'"])
		run_command("git push")
		print(fmtstr("[deploy][success] Success!", "green"))
	except CommandError as command_error:
		print(fmtstr("[deploy][error] %s" % command_error, "red"))

# import subprocess
# cmd = ['/run/myscript', '--arg', 'value']
# p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
# for line in p.stdout:
#     print line
# p.wait()
# print p.returncode	