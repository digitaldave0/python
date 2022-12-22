import boto3
import uuid
s3 = boto3.resource('s3')

#Reads list and creates s3-buckets but you need to add LocationConstraint to get this to work
bucket_names = ['dah-bucket1-{}'.format(uuid.uuid4()), 'dah-bucket2-{}'.format(uuid.uuid4()), 'dah-bucket3-{}'.format(uuid.uuid4())]

for y in bucket_names:
    print ('Creating new buckets from list {}'.format(y))
    s3.create_bucket(Bucket=(y), CreateBucketConfiguration={'LocationConstraint': 'eu-west-2'})


