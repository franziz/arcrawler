from lib.shell import Shell
import shutil
import os

if __name__ == "__main__":
	source_name   = input("Source Name: ")
	source_origin = input("Source Origin: ")

	print("[new_source][debug] Removing source folder...")
	shutil.rmtree("/root/app/src")

	print("[new_source][debug] Making new source folder...")
	os.mkdir("/root/app/src")
	os.chdir("/root/app/src")

	Shell.run_command("git init")
	Shell.run_command("git config --global push.default current")
	Shell.run_command("git remote add origin http://github.com/isidsea/engine_sources.git")
	Shell.run_command("git remote update --prune")
	Shell.run_command("git checkout -b %s" % source_name)
	Shell.run_command("git pull origin %s" % source_origin)
	Shell.run_command("git push -u origin %s" % source_name)

