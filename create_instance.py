import boto3

def create_test():
    ec2 = boto3.resource('ec2')
    instances = ec2.create_instances(
    ImageId='ami-0127cb92c2ac61534',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro')

    instances[0].wait_until_running()
    print(instances[0].id)

create_test()