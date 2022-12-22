import os
import boto3
import boto3.session as Client

global session
session = boto3.Session(region_name='us-east-1',
                            aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
                            aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
                            aws_session_token=os.environ['AWS_SESSION'])

#use boto s3
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
  print(bucket.name)

# Upload a new file from local to s3 bucket ab
data = open('images/Firefox_wallpaper.png', 'rb')
s3.Bucket('dah-test').put_object(Key='Firefox_wallpaper.png', Body=data)

#use boto client library to download file from s3 bucket to local machine

s3client = boto3.client('s3')
s3client.download_file('dah-test', 'Firefox_wallpaper.png', 'images/client_Firefox_wallpaper.png')