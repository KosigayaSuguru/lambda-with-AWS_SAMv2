import json
import sys

# 以降、レイヤー用のimport（環境変数のPYTHONPATHに/optを通す方がスマートだけど。。）
sys.path.append('/opt')  # nopep8


def lambda_handler(event, context):

    import threading
    threads = []
    for idx in range(10):
        t = threading.Thread(name="thread1", target=exec_dataset)
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world@function_db",
        }),
    }


def exec_dataset():
    from .db import con
    results = con.query('select count(*) as cnt from test1 as t1,test1 as t2, test1 as t3, test1 as t4, test1 as t5, test1 as t6;')
    for record in results:
        print(record['cnt'])
    # con.close() # conをclose()すると動かなくなる。。
