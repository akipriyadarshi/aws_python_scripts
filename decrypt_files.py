import glob
from cryptography.fernet import Fernet
from pathlib import Path
import os

# opening the key
with open('filekey.key', 'rb') as filekey:
    key = filekey.read()

# using the key
fernet = Fernet(key)

files= glob.glob("/home/knoldus/Desktop/files_to_be_encrypted/*")
os.chdir("/home/knoldus/Desktop/files_to_be_encrypted")
path= os.getcwd()

# opening the encrypted file
for filename in files:
	with open(filename, 'rb') as enc_file:
		encrypted = enc_file.read()
		decrypted = fernet.decrypt(encrypted)
		with open(filename, 'wb') as dec_file:
			dec_file.write(decrypted)
	base=os.path.basename(filename)
	dest=path+"/"+os.path.splitext(base)[0]+".decrypt"
	os.rename(filename,dest)
  
# decrypting the file
#decrypted = fernet.decrypt(encrypted)
  
# opening the file in write mode and
# writing the decrypted data
#for filename in files:
#	with open(filename, 'wb') as dec_file:
#		dec_file.write(decrypted)
