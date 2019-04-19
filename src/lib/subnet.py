from enum import Enum
import boto3

client = boto3.client('ec2')


def subnet_ids(Enum):
    return (
        "subnet-5e827f28",
        "subnet-11ded148",
    )


def get_availability_zone(subnet_id: str):
    return _describe_subnet(subnet_id)['AvailabilityZone']


def get_available_ip_address_count(subnet_id: str):
    return _describe_subnet(subnet_id)['AvailableIpAddressCount']


def _describe_subnet(subnet_id: str):
    response = client.describe_subnets(
        SubnetIds=[subnet_id]
    )

    if len(response['Subnets']) == 1:
        return response['Subnets'][0]
    else:
        raise 'DescribeSubnetsError'
