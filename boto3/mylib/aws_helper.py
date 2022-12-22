# aws helper file for functions used a lot

import boto3
import csv
import logging



def assume_role(role_arn, role_session_name):
    # Create a new STS client
    sts_client = boto3.client("sts")

    # Assume the role and get the resulting credentials
    response = sts_client.assume_role(
        RoleArn=role_arn,
        RoleSessionName=role_session_name
    )
    return response["Credentials"]


# logger function

def setup_logger():
    # Set up a logger with the specified format and log level
    logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s", level=logging.INFO)


# list quotas and write to csv file

def list_service_quotas(service_code, region):
    # Create a new Service Quotas client
    client = boto3.client("servicequotas")

    # List all service quotas for the service
    result = client.list_service_quotas(ServiceCode=service_code, Region=region)

    # Write the quotas to a CSV file
    write_to_csv(result["Quotas"])

# write to csv file

def write_to_csv(quotas):
    # Open the CSV file in append mode
    with open("quotas.csv", "a", newline="") as csvfile:
        # Create a CSV writer
        writer = csv.writer(csvfile)

        # Write the header row
        writer.writerow(["Quota Name", "Quota Value", "Quota Unit"])

        # Write the quotas
        for quota in quotas:
            writer.writerow([quota["QuotaName"], quota["Value"], quota["Unit"]])

# retrive object from bucket

def get_object_from_s3(bucket, key):
    s3 = boto3.client("s3")
    response = s3.get_object(Bucket=bucket, Key=key)
    data = response["Body"].read()
    return data

# insert item into dyamodb table

def put_item_into_dynamodb(table_name, item):
    dynamodb = boto3.client("dynamodb")
    dynamodb.put_item(TableName=table_name, Item=item)

# cloud watch put metric

def put_custom_metric_into_cloudwatch(namespace, metric_name, value, unit, dimensions):
    cloudwatch = boto3.client("cloudwatch")
    cloudwatch.put_metric_data(
        Namespace=namespace,
        MetricData=[
            {
                "MetricName": metric_name,
                "Unit": unit,
                "Value": value,
                "Dimensions": dimensions,
            },
        ],
    )
