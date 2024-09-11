import boto3
import json
import os
import argparse
import sys

def get_all_task_definitions(ecs_client):
    try:
        # List all task definition ARNs
        task_definitions = []
        paginator = ecs_client.get_paginator('list_task_definitions')
        for page in paginator.paginate():
            task_definitions.extend(page['taskDefinitionArns'])
        return task_definitions
    except Exception as e:
        print(f"Error retrieving task definitions: {e}")
        sys.exit(1)

def describe_task_definition(ecs_client, task_definition_arn):
    try:
        # Retrieve the details of a specific task definition
        response = ecs_client.describe_task_definition(taskDefinition=task_definition_arn)
        return response['taskDefinition']
    except Exception as e:
        print(f"Error retrieving task definition for ARN {task_definition_arn}: {e}")
        return None

def dump_task_definition_to_file(task_definition, folder_path):
    # Create a file name from the task definition family and revision
    task_family = task_definition['family']
    task_revision = task_definition['revision']
    file_name = f"{task_family}_rev_{task_revision}.json"
    
    # Full path for the file
    file_path = os.path.join(folder_path, file_name)
    
    try:
        # Write the task definition to a JSON file
        with open(file_path, 'w') as f:
            json.dump(task_definition, f, indent=4)
        print(f"Task definition {task_family} revision {task_revision} dumped to {file_path}")
    except Exception as e:
        print(f"Error writing task definition to file {file_path}: {e}")

def ensure_folder_exists(folder_path):
    try:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created folder: {folder_path}")
    except Exception as e:
        print(f"Error creating folder {folder_path}: {e}")
        sys.exit(1)

def dump_task_definitions_to_folder(region, account_id, folder_path):
    # Initialize the ECS client
    ecs_client = boto3.client('ecs', region_name=region)
    
    # Ensure the folder exists
    ensure_folder_exists(folder_path)
    
    # Get all task definition ARNs
    all_task_definitions = get_all_task_definitions(ecs_client)
    
    for task_definition_arn in all_task_definitions:
        task_definition = describe_task_definition(ecs_client, task_definition_arn)
        if task_definition:
            dump_task_definition_to_file(task_definition, folder_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Dump ECS task definitions to JSON files.')
    parser.add_argument('--region', required=True, help='AWS region to use')
    parser.add_argument('--account', required=True, help='AWS account ID (not used in this script but included for completeness)')
    parser.add_argument('--output-folder', required=True, help='Folder to save the dumped task definitions')

    args = parser.parse_args()
    
    # Dump task definitions to the specified folder
    dump_task_definitions_to_folder(args.region, args.account, args.output_folder)
