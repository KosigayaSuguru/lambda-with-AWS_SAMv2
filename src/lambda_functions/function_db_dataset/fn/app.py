import json
import sys

# 以降、レイヤー用のimport（環境変数のPYTHONPATHに/optを通す方がスマートだけど。。）
sys.path.append('/opt')  # nopep8


def lambda_handler(event, context):

    from .db import con

    # スレッドでSQL実行
    thread_run_exec_dataset(10)

    # # 普通にSQL実行
    # exec_dataset()

    close_and_monitor(con)
    wait_and_countdown(5)

    # スレッドでSQL実行
    thread_run_exec_dataset(10)

    # # 普通にSQL実行
    # exec_dataset()

    close_and_monitor(con)
    wait_and_countdown(5)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world@function_db",
        }),
    }


def exec_dataset():
    from .db import con
    results = con.query(
        'select count(*) as cnt from ' +
        'test1 as t1, test1 as t2, test1 as t3, test1 as t4, test1 as t5, ' +
        'test1 as t6, test1 as t7, test1 as t8, ' +
        'test1 as t100;'
    )

    for record in results:
        print(record['cnt'])
    # con.close()  # conをclose()すると動かなくなる。。


def thread_run_exec_dataset(threads):
    import threading
    thread_list = []
    for idx in range(threads):  # threadsはスレッド数
        t = threading.Thread(name="thread1", target=exec_dataset)
        t.start()
        thread_list.append(t)

    for thread in thread_list:
        thread.join()


def wait_and_countdown(sec):
    for idx in range(sec):
        import time
        time.sleep(1)
        print(idx)


def close_and_monitor(con):
    print(f"con.executable.closed     : {con.executable.closed}")
    print(f"con.executable.invalidated: {con.executable.invalidated}")
    print(f"con.engine.pool.status()  : {con.engine.pool.status()}")
    # con.close()
    # con.executable.close()
    # con.executable.invalidate()
    # con.executable.engine.dispose()
    print(f"con.executable.closed     : {con.executable.closed}")
    print(f"con.executable.invalidated: {con.executable.invalidated}")
    print(f"con.engine.pool.status()  : {con.engine.pool.status()}")
