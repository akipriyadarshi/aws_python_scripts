import boto3

sess = boto3.Session()

# Creating lists for all, used, and unused key pairs
all_key_pairs = []
all_used_key_pairs = []
all_unused_key_pairs = []


# List the key pairs in the selected region
ec2 = sess.client('ec2')
all_key_pairs = list(map(lambda i: i['KeyName'], ec2.describe_key_pairs()['KeyPairs']))


print(all_key_pairs)


# Each EC2 reservation returns a group of instances.
instance_groups = list(map(lambda i: i['Instances'], ec2.describe_instances()['Reservations']))

# Create a list of all used key pairs in the account based on the running instances
for group in instance_groups:
  for i in group:
    if i['KeyName'] not in all_used_key_pairs:
      all_used_key_pairs.append(i['KeyName'])

print(all_used_key_pairs)


# Now compare the two lists
for key in all_key_pairs:
  if key not in all_used_key_pairs:
    all_unused_key_pairs.append(key)

print(all_unused_key_pairs)



# Delete all unused key pairs
print('Deleting unused key pairs:')
for key in all_unused_key_pairs:
  print(key)
  ec2.delete_key_pair(KeyName=key)