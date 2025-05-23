import os
import hashlib

DATA_EXT = ".data"
INDEX_EXT = ".idx"

def MD5_DATA(PACK_NAME):
	MD5_HASH = hashlib.md5()
	DATA_FILE = os.getcwd() + "\\" + PACK_NAME + DATA_EXT

	with open(DATA_FILE, "rb") as file:
		for byte in iter(lambda: file.read(4096),b""):
			MD5_HASH.update(byte)
		print(DATA_FILE + " : " + MD5_HASH.hexdigest())

def MD5_INDEX(PACK_NAME):
	MD5_HASH = hashlib.md5()
	INDEX_FILE = os.getcwd() + "\\" + PACK_NAME + INDEX_EXT

	with open(INDEX_FILE, "rb") as file:
		for byte in iter(lambda: file.read(4096),b""):
			MD5_HASH.update(byte)
		print(INDEX_FILE + " : " + MD5_HASH.hexdigest())

if __name__ == "__main__":
	PACK_NAME = raw_input("Enter the pack without extension : ")

	MD5_DATA(PACK_NAME)
	MD5_INDEX(PACK_NAME)

	os.system("pause")
