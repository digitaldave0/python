import os
import time
import logging
from azure.common.client_factory import get_client_from_cli_profile
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.compute.models import DiskCreateOption, VirtualMachine, VirtualMachineScaleSetVM
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.resource.resources.models import ResourceGroup

def create_vm(vm_name, resource_group_name, vm_size, disk_size_gb, memory_gb, progress_callback=None):
    # Get the Azure management clients
    compute_client = get_client_from_cli_profile(ComputeManagementClient)
    resource_client = get_client_from_cli_profile(ResourceManagementClient)

    # Create a resource group
    resource_client.resource_groups.create_or_update(
        resource_group_name,
        ResourceGroup(location="westus2")
    )

    # Create a managed disk
    logging.info("Creating managed disk...")
    disk_name = vm_name + "-disk"
    async_disk_creation = compute_client.disks.begin_create_or_update(
        resource_group_name,
        disk_name,
        {
            "location": "westus2",
            "disk_size_gb": disk_size_gb,
            "creation_data": {
                "create_option": DiskCreateOption.empty
            }
        }
    )
    disk_resource = async_disk_creation.result()
    logging.info("Managed disk created successfully")

    # Create a virtual machine
    logging.info("Creating virtual machine...")
    vm_parameters = {
        "location": "westus2",
        "os_profile": {
            "computer_name": vm_name,
            "admin_username": "azureuser",
            "admin_password": "azureuser!23"
        },
        "hardware_profile": {
            "vm_size": vm_size
        },
        "storage_profile": {
            "image_reference": {
                "publisher": "Canonical",
                "offer": "UbuntuServer",
                "sku": "20.04-LTS",
                "version": "latest"
            },
            "os_disk": {
                "name": vm_name + "-osdisk",
                "caching": "ReadWrite",
                "create_option": "FromImage",
                "managed_disk": {
                    "id": disk_resource.id
                }
            }
        },
        "network_profile": {
            "network_interfaces": [{
                "id": network_interface.id,
            }]
        }
    }
    async_vm_creation = compute_client.virtual_machines.create_or_update(
        resource_group_name,
        vm_name,
        vm_parameters
    )
    vm_resource
