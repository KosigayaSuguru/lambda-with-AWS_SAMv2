import os
# print(os.getcwd())  # nopep8

import sys
# print(sys.path)  # nopep8
# sys.path.append(f'.{os.sep}src{os.sep}lambda_functions')  # nopep8
# sys.path.append(f'.{os.sep}src{os.sep}layer{os.sep}python')  # nopep8

from function_db_dataset.fn import app


app.lambda_handler(None, None)
