from lib.builder import Builder
from curtsies    import fmtstr

if __name__ == "__main__":
	try:
		Builder.build()
	except Exception as ex:
		print(fmtstr("[build][error] %s" % ex,"red"))