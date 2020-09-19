import json
import sys

# 以降、レイヤー用のimport（環境変数のPYTHONPATHに/optを通す方がスマートだけど。。）
sys.path.append('/opt')  # nopep8
import dataset


def lambda_handler(event, context):

    con = dataset.connect('mysql://root:password@localhost:33306/hoge')
    print(con)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world@function_db",
        }),
    }
