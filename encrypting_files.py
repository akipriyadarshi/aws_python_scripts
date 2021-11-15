import glob
import os
from cryptography.fernet import Fernet
from pathlib import Path


# opening the key
with open('filekey.key', 'rb') as filekey:
    key = filekey.read()
  
# using the generated key
fernet = Fernet(key)

files= glob.glob("/home/knoldus/Desktop/files_to_be_encrypted/*")
os.chdir("/home/knoldus/Desktop/files_to_be_encrypted")
path= os.getcwd()

  
# opening the original file to encrypt
for filename in files:
	with open(filename, 'rb') as file:
		original = file.read()
		encrypted = fernet.encrypt(original)
		with open(filename, 'wb') as encrypted_file:
			encrypted_file.write(encrypted)
	base=os.path.basename(filename)
	dest=path+"/"+os.path.splitext(base)[0]+".encrypt"
	os.rename(filename,dest)
      
# encrypting the file
# encrypted = fernet.encrypt(original)
  
# opening the file in write mode and 
# writing the encrypted data

#for filename in files:
#	with open(filename, 'wb') as encrypted_file:
#		encrypted_file.write(encrypted)
