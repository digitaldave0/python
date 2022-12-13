
import boto3

def list_mybuckets():
    s3 = (boto3.resource('s3'))
    for bucket in (s3.buckets.all()):
        print (bucket.name)
        print ("---")
    for item in bucket.objects.all():
        print ("\t%s" % item.key)

list_mybuckets()