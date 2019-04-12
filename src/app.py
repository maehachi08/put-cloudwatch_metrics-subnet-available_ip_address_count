import json
import traceback
from botocore.exceptions import ClientError

from lib import enum, subnet, cloudwatch


def lambda_handler(event, context):
    try:
        response = {}
        for subnet_id in enum.subnet_ids:
            availability_zone = subnet.get_availability_zone(subnet_id)
            available_ip_address_count = subnet.get_available_ip_address_count(subnet_id)
            put_metric_data_response = cloudwatch.put_metric_data_wrapper(subnet_id, availability_zone, available_ip_address_count)
            response[subnet_id] = put_metric_data_response

        return response

    except ClientError as e:
        print(traceback.format_exc())


if __name__ == '__main__':
    response = lambda_handler({}, {})
    print(
        json.dumps(
            response,
            indent=4,
            sort_keys=True
        )
    )

