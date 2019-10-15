import json
import sys

sys.path.append('/opt')

from service import hoge_service


def lambda_handler(event, context):
    hoge_service.hoge()

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        }),
    }
