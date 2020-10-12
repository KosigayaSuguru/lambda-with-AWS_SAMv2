import sys

# 以降、レイヤー用のimport（環境変数のPYTHONPATHに/optを通す方がスマートだけど。。）
sys.path.append('/opt')  # nopep8
import dataset

from sqlalchemy.pool import NullPool

con = dataset.connect(
    'mysql://root:password@172.17.0.1:3306/hoge?charset=utf8mb4',
    engine_kwargs={
        # 'poolclass': NullPool, # コネクションプールを使いたくない時
        'pool_size': 10,
        'max_overflow': 0,  # 0以外を指定すると、pool_sizeを超えてくるので注意
        # 'pool_recycle': 2,
        # 'echo': True,
        # 'echo_pool': True,
        # 'pool_pre_ping': True,
    }
)
