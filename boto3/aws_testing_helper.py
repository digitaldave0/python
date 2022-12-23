# main.py

import aws_helper
import boto3

aws_helper.setup_logger()
aws_helper.logging.info("Starting Service Quota Logining")
aws_helper.list_service_quotas("ec2", "eu-west-1")


# Assume the role and get the resulting credentials
credentials = aws_helper.assume_role("arn:aws:iam::123456789012:role/MyRole", "MySession")

# Use the credentials to create a new client
client = boto3.client("ec2", aws_access_key_id=credentials["AccessKeyId"],
    aws_secret_access_key=credentials["SecretAccessKey"],
    aws_session_token=credentials["SessionToken"])

# Use the client to list the EC2 instances
response = client.describe_instances()
print(response)
