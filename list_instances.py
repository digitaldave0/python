import boto3


def my_list():
    ec2 = boto3.resource('ec2')

    for instance in ec2.instances.all():
            print (instance.tags)
            for tag in instance.tags:
                    print(tag['Value'])
my_list()

