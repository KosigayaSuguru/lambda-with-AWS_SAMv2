import sys

# 以降、レイヤー用のimport（環境変数のPYTHONPATHに/optを通す方がスマートだけど。。）
sys.path.append('/opt')  # nopep8
import dataset

from sqlalchemy.pool import NullPool

con = dataset.connect('mysql://root:password@host.docker.internal:33306/hoge',
                      engine_kwargs={
                          # 'poolclass': NullPool, # コネクションプールを使いたくない時
                          'pool_size': 10,
                      }
                      )
