import json
import sys

sys.path.append('/opt')
from service import hoge_service
from .mycode import code


def lambda_handler1(event, context):
    hoge_service.hoge()

    code.code()

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        }),
    }


def lambda_handler2(event, context):
    hoge_service.hoge()

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        }),
    }
