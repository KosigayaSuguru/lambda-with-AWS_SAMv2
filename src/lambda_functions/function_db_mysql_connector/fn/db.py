import json
import sys

# 以降、レイヤー用のimport（環境変数のPYTHONPATHに/optを通す方がスマートだけど。。）
sys.path.append('/opt')  # nopep8
import mysql.connector

def get_connection():
    # 何回コールしても同じ接続情報を返してる
    # ※呼び出すたびに接続が10増えることは無く、設定したプールで実行される（プール数超えて同時実行しようとするとエラーになる）
    return mysql.connector.connect(user='root', password='password',
                                  host='host.docker.internal',
                                  port='33306',
                                  database='hoge',
                                  pool_size=10,
                                  )
