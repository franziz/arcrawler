from lib.engine.converter import ConverterEngine
from curtsies             import fmtstr
import time
import random

if __name__ == "__main__":
	while True:
		engine = ConverterEngine()
		engine.convert()

		rnd = random.randint(60,500)
		print(fmtstr("Sleeping %s seconds" % rnd,"yellow"))
		time.sleep(rnd)
		