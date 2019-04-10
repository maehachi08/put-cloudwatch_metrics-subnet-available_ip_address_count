import json
import pytest

import app


def test_lambda_handler():
    response = app.lambda_handler({}, {})
    print(
        json.dumps(
            response,
            indent=4,
            sort_keys=True
        )
    )
