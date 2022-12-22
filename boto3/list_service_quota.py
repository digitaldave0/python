import boto3
import botocore.client as Client

response = Client.get_aws_default_service_quota(
    ServiecName='string',
    ServiceCode='string',
    QuotaCode='string'
)