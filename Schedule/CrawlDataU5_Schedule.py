import os
import sys
import time
_get_module_path = os.path.normpath(os.path.join(os.getcwd(), os.path.dirname(__file__), ''))
sys.path.append(_get_module_path + "/../Class")
from FreeProxyIplManager import FreeProxyIplManagerClass

class CrawlDataU5_Schedule(object):
    def __init__(self):
        pass
    #主要方法
    def main(self):
        func = FreeProxyIplManagerClass.crawl_data5u()
        func_name = getattr(func, '__name__', "None")
        print(format(func_name))
        for proxy in func:
            print(proxy)
def run():  
    print ("主进程: %s" % os.getppid())
    print ("子进程: %s" % os.getpid())
    CrawlDataU5_ScheduleClass = CrawlDataU5_Schedule()
    CrawlDataU5_ScheduleClass.main()

run()

