import boto3
import csv

import csv

def write_quotas_to_csv(quotas):
    # Open the CSV file in append mode
    with open("quotas.csv", "a", newline="") as csvfile:
        # Create a CSV writer
        writer = csv.writer(csvfile)

        # Write the header row
        writer.writerow(["Quota Name", "Quota Value", "Quota Unit"])

        # Write the quotas
        for quota in quotas:
            writer.writerow([quota["QuotaName"], quota["Value"], quota["Unit"]])


def list_service_quotas(service_code, region):
    # Create a new Service Quotas client
    client = boto3.client("servicequotas")

    # List all service quotas for the service
    result = client.list_service_quotas(ServiceCode=service_code, Region=region)

    # Open the CSV file in append mode
    with open("quotas.csv", "a", newline="") as csvfile:
        # Create a CSV writer
        writer = csv.writer(csvfile)

        # Write the header row
        writer.writerow(["Quota Name", "Quota Value", "Quota Unit"])

        # Write the quotas
        for quota in result["Quotas"]:
            writer.writerow([quota["QuotaName"], quota["Value"], quota["Unit"]])
