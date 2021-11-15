import boto3

s3=boto3.client('s3')
s3.upload_file('/home/knoldus/Desktop/s3upload.txt','s3uploadtestbucket-aki','s3script.txt')

# for deletion
# s3 = boto3.resource('s3')
# s3.Object('your-bucket', 'your-key').delete()



