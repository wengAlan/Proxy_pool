#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     proxy_pool_run.py  
   Description :  代理池采集运行主文件
   Author :       Alan
   date：         2020/01/19
-------------------------------------------------
-------------------------------------------------
"""
__author__ = 'Alan'

import sys
import signal
from multiprocessing import Process,cpu_count
import os
dir_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir_path)
sys.path.append(dir_path+'/')
sys.path.append(dir_path+'/../')
sys.path.append(dir_path+'/../../')

from Schedule.Baidu_DistributionSchedule import run as Baidu_Distribution_Run
from settings import settings_yq_process as yq_settings
def run():
    cpu_num = cpu_count()
    p_list = list()
    #百度新增处理经常
    p0 = Process(target=Baidu_Distribution_Run, name='Baidu_Distribution_Run',args=(yq_settings.BAI_DUI_QUEUE['pressing'],yq_settings.QUEUE_REDIS_SERVER,yq_settings.BAIDUI_REQUEST_URL))
    p_list.append(p0)
    p1 = Process(target=Baidu_Distribution_Run, name='Baidu_Distribution_Run',args=(yq_settings.BAI_DUI_QUEUE['newst'],yq_settings.QUEUE_REDIS_SERVER,yq_settings.BAIDUI_REQUEST_URL))
    p_list.append(p1)
    p2 = Process(target=Baidu_Distribution_Run, name='Baidu_Distribution_Run',args=(yq_settings.BAI_DUI_QUEUE['old'],yq_settings.QUEUE_REDIS_SERVER,yq_settings.BAIDUI_REQUEST_URL))
    p_list.append(p2)
    p3 = Process(target=Baidu_Distribution_Run, name='Baidu_Distribution_Run',args=(yq_settings.BAI_DUI_QUEUE['abnormal'],yq_settings.QUEUE_REDIS_SERVER,yq_settings.BAIDUI_REQUEST_URL))
    p_list.append(p3)

    def kill_child_processes(signum, frame):
        for p in p_list:
            p.terminate()
        sys.exit(1)

    signal.signal(signal.SIGTERM, kill_child_processes)

    for p in p_list:
        p.daemon = True
        p.start()
        
    for p in p_list:
        p.join()

if __name__ == '__main__':
    run()
