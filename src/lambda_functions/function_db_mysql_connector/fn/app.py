import json
import sys

# 以降、レイヤー用のimport（環境変数のPYTHONPATHに/optを通す方がスマートだけど。。）
sys.path.append('/opt')  # nopep8
import mysql.connector


def lambda_handler(event, context):

    import threading
    threads = []
    for idx in range(10):
        t = threading.Thread(name="thread1", target=exec_mysql_connector)
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


def exec_mysql_connector():
    from .db import get_connection

    cnx = get_connection()
    cursor = cnx.cursor()
    # cursor.execute('select count(*) from test1 as t1,test1 as t2, test1 as t3, test1 as t4, test1 as t5, test1 as t6, test1 as t7;')
    cursor.execute('select count(*) from test1 as t1,test1 as t2, test1 as t3, test1 as t4, test1 as t5, test1 as t6;')
    # cursor.execute('select * from test1 as t1;')
    for record in cursor:
        print(record)
        pass

    cursor.close()
    cnx.close()
