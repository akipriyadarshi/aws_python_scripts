## In order to delete a user we need to
 ## 1. Delete login profile of user
 ## 2. Dettach user policy from user
 ## 3. Delete access keys
 ## 4. Delete user

import boto3
import datetime
iam = boto3.client('iam')
user_name=[]

def timeDiff(create_time, current_time):
    running_time = current_time - create_time
    return running_time.seconds/60




for user in iam.list_users()['Users']:
    print(user["UserName"])
    time=timeDiff(user['CreateDate'], datetime.datetime.now(user['CreateDate'].tzinfo))
    print(time)
    if time>1 and user['UserName']!='Root':    #change the time in minutes according to your need
        user_name.append(user['UserName'])
    
print(user_name)



######################################### 1. Delete Login Profile of user ##################################
for user in user_name:
    iam.delete_login_profile(UserName=user)
############################################################################################################





################################# 2. Dettach policy from user  #######################################################
iam= boto3.resource('iam')
for user in user_name:
    user1 = iam.User(user)
    user1.detach_policy(PolicyArn='arn:aws:iam::572163513905:policy/ec2-readonly-2')

######################################################################################################################




################################### 3. Retrieve and Delete Access Key ID  ############################################################
iam = boto3.client('iam')

paginator = iam.get_paginator('list_access_keys')
for user in user_name:
    for response in paginator.paginate(UserName=user):
        access_id=response['AccessKeyMetadata'][0]['AccessKeyId']
        iam.delete_access_key(AccessKeyId=access_id, UserName=user)


#################################################### 4. Delete users #################################################################################

for user in user_name:
    iam.delete_user(UserName=user)

######################################################################################################################################################




