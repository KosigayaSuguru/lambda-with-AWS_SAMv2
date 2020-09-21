import os
# print(os.getcwd())  # nopep8

import sys
# print(sys.path)  # nopep8
# sys.path.append(f'.{os.sep}src{os.sep}lambda_functions')  # nopep8
# sys.path.append(f'.{os.sep}src{os.sep}layer{os.sep}python')  # nopep8

from function1.fn import app


app.lambda_handler1(None, None)
