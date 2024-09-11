import boto3
import json
import os
import argparse
from datetime import datetime, timedelta

def dump_ssm_parameters_to_json(region, output_folder):
    ssm_client = boto3.client('ssm', region_name=region)
    parameters = []
    next_token = None
    
    # Calculate the cutoff date for the last 6 months
    six_months_ago = datetime.now() - timedelta(days=6*30)  # Approximate 6 months

    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    while True:
        try:
            # Retrieve parameters
            if next_token:
                response = ssm_client.describe_parameters(MaxResults=50, NextToken=next_token)
            else:
                response = ssm_client.describe_parameters(MaxResults=50)
            
            # Filter secure string parameters
            for param in response.get('Parameters', []):
                if param['Type'] == 'SecureString':
                    # Fetch parameter metadata
                    param_metadata = ssm_client.get_parameter_history(Name=param['Name'], MaxResults=1)
                    if param_metadata['Parameters']:
                        # Check the last modified date
                        last_modified_date = param_metadata['Parameters'][0]['LastModifiedDate']
                        if last_modified_date >= six_months_ago:
                            # Fetch parameter value
                            parameter = ssm_client.get_parameter(Name=param['Name'], WithDecryption=True)
                            parameters.append({
                                'Name': parameter['Parameter']['Name'],
                                'Value': parameter['Parameter']['Value']
                            })

            # Check for pagination
            next_token = response.get('NextToken')
            if not next_token:
                break
        
        except Exception as e:
            print(f"An error occurred: {e}")
            break

    # Define the output file path
    output_file = os.path.join(output_folder, 'ssm_parameters.json')

    # Write parameters to JSON file
    with open(output_file, 'w') as f:
        json.dump(parameters, f, indent=4)

    print(f"SSM parameters dumped to {output_file}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Dump SecureString SSM parameters to a JSON file.')
    parser.add_argument('--region', required=True, help='AWS region to use')
    parser.add_argument('--account', required=True, help='AWS account ID (not used in this script but included for completeness)')
    parser.add_argument('--output-folder', required=True, help='Folder to save the dumped SSM parameters')

    args = parser.parse_args()
    
    # Dump SSM parameters to the specified folder
    dump_ssm_parameters_to_json(args.region, args.output_folder)
