from lib.exceptions import CommandError
from lib.shell      import Shell
from curtsies       import fmtstr
import os

if __name__ == "__main__":
	try:
		source_target = input("Merge to: ")

		os.chdir("/root/app/src")
		err_code, output = Shell.run_command("git status")
		output           = output[0]
		current_branch   = output.replace("On branch ","")
		current_branch   = current_branch.replace("\n","")
		
		Shell.run_command("git add --all .")
		Shell.run_command(["git", "commit", "-m" ,"'Automated commit from merge_source.py'"])
		Shell.run_command("git checkout -b %s" % source_target, ignore_error=True)
		Shell.run_command("git pull origin %s" % source_target)
		
		exit_code, output = Shell.run_command("git merge %s" % current_branch)
		Shell.run_command("git push origin %s" % source_target)
	except CommandError as command_error:
		print(fmtstr("[merge_source][error] %s" % command_error,"red"))
		print("[merge_source][error] Rolling back...")
		Shell.run_command("git checkout %s" % current_branch)
