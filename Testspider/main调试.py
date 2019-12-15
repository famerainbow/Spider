import sys
import os
from scrapy.cmdline import execute
#sys.path.append('F:\pycharm\PyCharm Community Edition 2018.2.2\project/Testspider')
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(['scrapy','crawl','test'])