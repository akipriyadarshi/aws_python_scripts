import boto3
import datetime
ec2 = boto3.resource('ec2')
id=[]
# for instance in ec2.instances.all():
#      print(
#          "Id: {0}\nPlatform: {1}\nType: {2}\nPublic IPv4: {3}\nAMI: {4}\nState: {5}\n".format(
#          instance.id, instance.platform, instance.instance_type, instance.public_ip_address, instance.image.id, instance.state
#          )
#      )


def timeDiff(launch_time, current_time):
    running_time = current_time - launch_time
    return running_time.seconds/60


for instance in ec2.instances.all():
    if instance.state['Name']!='terminated':
        print(instance.id)
        print(instance.launch_time)
        time=timeDiff(instance.launch_time, datetime.datetime.now(instance.launch_time.tzinfo))
        print(time)
        if time>1:
            id.append(instance.id)

          

print(id)
#ec2.instances.filter(InstanceIds = id).terminate()


