from pathlib import Path
import glob
import os


files= glob.glob("/home/knoldus/Desktop/files_to_be_encrypted/*")

os.chdir("/home/knoldus/Desktop/files_to_be_encrypted")
path= os.getcwd()




for filename in files:
	base=os.path.basename(filename)
	dest=path+"/"+os.path.splitext(base)[0]+".encrypt"
	os.rename(filename,dest)



#print("File      Path:", Path(__file__).absolute())
#print("Directory Path:", Path().absolute())


