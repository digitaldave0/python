# awsutils

import boto3

def get_session(region):
    return boto3.session.Session(region_name=region)

def create_ec2(count):
    ec2 = boto3.resource('ec2')
    instance = ec2.create_instances(
    Count = (count),
    ImageId=('006a0174c6c25ac06'),
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro')
print (instance[0].id)

create_ec2(count)