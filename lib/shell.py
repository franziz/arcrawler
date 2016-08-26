from .exceptions import CommandError
import subprocess

class Shell:
	def __init__(self):
		pass

	@staticmethod
	def run_command(command=None, ignore_error=False):
		assert command is not None, "command is not defined."
		command = command.split(" ") if not type(command) is list else command
		print("[sheel][debug] Excuting: %s" % " ".join(command))
		
		proc    = subprocess.Popen(command, stdout=subprocess.PIPE)
		success = False
		output  = []
		for line in proc.stdout:
			line = line.decode("utf-8")
			output.append(line)
			if "nothing to commit" in line:
				success = True
		proc.wait()

		exit_code = proc.returncode
		if not ignore_error:
			if exit_code != 0 and not success: raise CommandError("Exit: %s" % exit_code)
		return (proc.returncode, output)