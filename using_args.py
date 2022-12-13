import argparse
import boto3
import botocore
import os
import pandas as pd
from boto3.s3.transfer import TransferConfig

def environment_set(access_key,secret_access_key):
    os.environ["AWS_ACCESS_KEY_ID"] = access_key
    os.environ["AWS_SECRET_ACCESS_KEY"] = secret_access_key

def s3_upload_file(args):     
 while True:
    try:
        s3 = boto3.resource('s3')

        GB = 1024 ** 3

            # Ensure that multipart uploads only happen if the size of a transfer
            # is larger than S3's size limit for nonmultipart uploads, which is 5 GB.
        config = TransferConfig(multipart_threshold=5 * GB)

        s3.meta.client.upload_file(args.path, args.bucket, os.path.basename(args.path),Config=config)
        print ("S3 Uploading successful")
        break
    except botocore.exceptions.EndpointConnectionError:
      print ("Network Error: Please Check your Internet Connection")
    except Exception as e:
      print (e)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='UPLOAD A FILE TO PRE-EXISTING S3 BUCKET')
    parser.add_argument('path', metavar='PATH', type=str,
            help='Enter the Path to file to be uploaded to s3')
    parser.add_argument('bucket', metavar='BUCKET_NAME', type=str,
            help='Enter the name of the bucket to which file has to be uploaded')
    parser.add_argument('cred', metavar='CREDENTIALS', type=str,
            help='Enter the Path to credentials.csv, having AWS access key and secret access key')    
    args = parser.parse_args()
    df = pd.read_csv(args.cred, header=None)
    access_key = df.iloc[1,1]
    secret_access_key = df.iloc[1,2]
    environment_set(access_key,secret_access_key)
    s3_upload_file(args)