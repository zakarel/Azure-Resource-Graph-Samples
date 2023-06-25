from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.compute.models import VirtualMachineSizeTypes
from

credential = DefaultAzureCredential()
compute_client = ComputeManagementClient(credential, 'CREDENTIAL_SUBSCRIPTION_ID')

region = "eastus"
cpu = 2
memory = 4
data_disk = 1

available_sizes = compute_client.virtual_machine_sizes.list(region)
filtered_sizes = [size for size in available_sizes if size.number_of_cores >= cpu and size.memory_in_mb >= memory and size.max_data_disk_count >= data_disk]

for size in filtered_sizes:
    print(size.name)