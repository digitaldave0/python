import boto3
import uuid
s3 = boto3.resource('s3')

#function to list buckets
def s3_listbucket():
    s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
  print (bucket.name)
  bucket.delete()
  


