import json
import os
import argparse

def json_to_hcl(task_definition, file_name):
    hcl_output = []
    
    # Start the resource block
    hcl_output.append(f'resource "aws_ecs_task_definition" "{task_definition["family"]}_rev_{task_definition["revision"]}" {{')
    
    # Family name
    hcl_output.append(f'  family = "{task_definition["family"]}"')
    
    # Container definitions as a string
    container_definitions = json.dumps(task_definition['containerDefinitions'], indent=2)
    hcl_output.append(f'  container_definitions = <<DEFINITION\n{container_definitions}\nDEFINITION')

    # Optional fields
    if task_definition.get('networkMode'):
        hcl_output.append(f'  network_mode = "{task_definition["networkMode"]}"')
    
    if task_definition.get('requiresCompatibilities'):
        compatibilities = json.dumps(task_definition['requiresCompatibilities'])
        hcl_output.append(f'  requires_compatibilities = {compatibilities}')
    
    if task_definition.get('cpu'):
        hcl_output.append(f'  cpu = "{task_definition["cpu"]}"')
    
    if task_definition.get('memory'):
        hcl_output.append(f'  memory = "{task_definition["memory"]}"')

    # Optional IAM roles
    if task_definition.get('taskRoleArn'):
        hcl_output.append(f'  task_role_arn = "{task_definition["taskRoleArn"]}"')
    
    if task_definition.get('executionRoleArn'):
        hcl_output.append(f'  execution_role_arn = "{task_definition["executionRoleArn"]}"')

    # Volumes
    if 'volumes' in task_definition and task_definition['volumes']:
        volumes = json.dumps(task_definition['volumes'], indent=2)
        hcl_output.append(f'  volumes = {volumes}')
    
    # Tags
    if 'tags' in task_definition and task_definition['tags']:
        tags = json.dumps(task_definition['tags'], indent=2)
        hcl_output.append(f'  tags = {tags}')
    
    # Close the resource block
    hcl_output.append('}\n')

    # Write the HCL to a file
    with open(file_name, 'w') as f:
        f.write('\n'.join(hcl_output))


def convert_json_to_hcl(input_directory, output_directory):
    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    # Iterate over each JSON file in the directory
    for file_name in os.listdir(input_directory):
        if file_name.endswith('.json'):
            file_path = os.path.join(input_directory, file_name)
            
            with open(file_path, 'r') as f:
                task_definition = json.load(f)
            
            # Define the output HCL file name
            hcl_file_name = f'{task_definition["family"]}_rev_{task_definition["revision"]}.tf'
            output_file_path = os.path.join(output_directory, hcl_file_name)
            
            # Convert JSON to HCL and write to the HCL file
            json_to_hcl(task_definition, output_file_path)
            print(f'Converted {file_name} to {hcl_file_name}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert JSON task definitions to Terraform HCL format.')
    parser.add_argument('--region', required=True, help='AWS region to use')
    parser.add_argument('--account', required=True, help='AWS account ID')
    parser.add_argument('--input-folder', required=True, help='Folder containing JSON task definition files')
    parser.add_argument('--output-folder', required=True, help='Folder to save Terraform HCL files')

    args = parser.parse_args()

    # Convert all JSON task definitions to Terraform HCL files
    convert_json_to_hcl(args.input_folder, args.output_folder)
