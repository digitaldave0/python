import os
import logging
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

def copy_folder_to_azure():
    # Prompt the user for the local folder path
    local_folder_path = input("Enter the local folder path: ")

    # Prompt the user for the Azure storage container name
    azure_container_name = input("Enter the Azure storage container name: ")

    # Prompt the user for the storage account name
    storage_account_name = input("Enter the storage account name: ")

    # Prompt the user for the storage account key
    storage_account_key = input("Enter the storage account key: ")

    # Create the BlobServiceClient object which will be used to create a container client
    blob_service_client = BlobServiceClient(
        f"https://{storage_account_name}.blob.core.windows.net",
        credential=storage_account_key
    )

    # Create the container client
    container_client = blob_service_client.get_container_client(azure_container_name)

    # Get a list of all files in the local folder
    local_files = os.listdir(local_folder_path)

    # Iterate through the list of local files and upload each one to Azure storage
    for file in local_files:
        # Create the BlobClient object
        blob_client = BlobClient(
            f"https://{storage_account_name}.blob.core.windows.net/{azure_container_name}/{file}", 
            credential=storage_account_key
        )

        # Open the local file in binary mode
        with open(os.path.join(local_folder_path, file), "rb") as data:
            # Upload the local file to Azure
            blob_client.upload_blob(data)
            logging.info(f"Successfully uploaded {file} to Azure storage")

# Example usage:
copy_folder_to_azure()