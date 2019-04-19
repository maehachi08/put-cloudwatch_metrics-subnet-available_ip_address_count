import json
import pytest

import app


def test_lambda_handler(mocker,):
    mocker.patch('lib.subnet.subnet_ids').return_value = ["subnet-123456789"]
    mocker.patch('lib.subnet.get_availability_zone').return_value = 'ap-northeast-1'
    mocker.patch('lib.subnet.get_available_ip_address_count').return_value = 100
    mocker.patch('lib.cloudwatch.put_metric_data_wrapper').return_value = {
        "ResponseMetadata": {
            "HTTPHeaders": {
                "content-length": "100",
                "content-type": "text/xml",
                "date": "Mon, 1 Apr 2019 12:00:00 GMT",
                "x-amzn-requestid": "bd3db6cd-6298-11e9-a7de-43111c66af9a"
            },
            "HTTPStatusCode": 200,
            "RequestId": "bd3db6cd-6298-11e9-a7de-43111c66af9a",
            "RetryAttempts": 0
        }
    }

    response = app.lambda_handler({}, {})

    # assert
    assert list(response.keys())[0] == 'subnet-123456789'

    print(
        json.dumps(
            response,
            indent=4,
            sort_keys=True
        )
    )
