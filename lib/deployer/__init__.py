from ..factory.config import ConfigFactory
import os
import zipfile
import requests

class Deployer:
	def zipdir(self, path, ziph):    
		for root, dirs, files in os.walk(path):
			for file in files:			
				ziph.write(os.path.join(root, file))

	def deploy(self):
		print("[deploy][debug] Zipping build folder...")
		zipf = zipfile.ZipFile('build.zip', 'w', zipfile.ZIP_DEFLATED)
		os.chdir(os.path.join(".","build"))
		self.zipdir(".", zipf)
		zipf.close()
		os.chdir(os.path.join(".."))

		print("[deploy][debug] Reading config...")
		route_config = ConfigFactory.get_config(ConfigFactory.ROUTE)
		route_config.reload(os.path.join(os.getcwd(),"build","config","route.json"))
		cd_server = route_config.get("cd_server")

		print("[deploy][debug] Sending the zip...")
		url  = "http://%s:%s/deploy?route=%s" % (cd_server["ip"], cd_server["port"], cd_server["route"])
		file = {"file":open("build.zip", "rb")}
		requests.post(url,files=file)

		print("[deploy][debug] Deleting the zip...")
		os.remove("build.zip")