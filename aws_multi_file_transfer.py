import glob
import boto3
import os

folder_name= '/home/knoldus/Desktop/s3upload'
bucket_name= 's3uploadtestbucket-aki'

# session = boto3.Session(profile_name='default')
 #s3 = session.client('s3')

s3=boto3.client('s3')

#csv_files = glob.glob("/home/user/folder1/c_log_*.csv")
#json_files = glob.glob("/home/user/folder1/h_log_*.json")
files= glob.glob("/home/knoldus/Desktop/s3upload/*")

for filename in files:
	#key = "%s/%s" % ('/home/knoldus/Desktop/s3upload', os.path.basename(filename))    this to put the data in directory structure in s3
	key= os.path.basename(filename)
	#print("Putting %s as %s" % (filename,key))
	s3.upload_file(filename, bucket_name, key)
	print(key)
     

#for filename in json_files:
 #   key = "%s/%s" % (FOLDER_NAME, os.path.basename(filename))
  #  print("Putting %s as %s" % (filename,key))
   # s3.upload_file(filename, BUCKET_NAME, key)

#print("All_Done")
