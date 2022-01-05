import sys
import init
import multi_menu

# init.main()
# multi_menu.main()

import os, sys
ret = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(ret)
print(os.path.abspath(__file__))
print(sys.path)
print(__name__)
import logging.config