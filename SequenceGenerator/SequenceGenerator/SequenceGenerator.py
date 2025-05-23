from random import randrange

def genKey():
	return randrange(0x0,0xfe)

def genLine():
	return " ".join(["0x%x," % genKey() for i in xrange(16)])

if __name__ == "__main__":
	with open("sequence.txt", "w") as seqFile:
		seqFile_write = seqFile.write
		seqFile_write("{\n")
		for i in xrange(2048):
			seqFile_write("\t%s\n" % genLine())
		seqFile_write("}\n")
