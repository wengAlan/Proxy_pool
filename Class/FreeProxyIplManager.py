# -*- coding: utf-8 -*-
# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      FreeProxyIplManager.py
   Description :   免费ip池抓取管理
   Author :        Alan
   date：          2020/01/19
-------------------------------------------------
-------------------------------------------------


"""
__author__ = 'Alan'

import re
import sys
import time
import requests

import os
_get_module_path = os.path.normpath(os.path.join(os.getcwd(), os.path.dirname(__file__), ''))
sys.path.append(_get_module_path + "/../Util")

from WebRequest import WebRequest
from utilFunction import getHtmlTree


"""
    免费ip池抓取管理  
"""
class FreeProxyIplManagerClass (object):

    @staticmethod
    def crawl_data5u():
        url = 'http://www.data5u.com/'
        html_tree = getHtmlTree(url)
        print(html_tree)
        ul_list = html_tree.xpath('//ul[@class="l2"]')
        key = 'ABCDEFGHIZ'
        for ul in ul_list:
            try:
                ip = ul.xpath('./span[1]/li/text()')[0]
                classnames = ul.xpath('./span[2]/li/attribute::class')[0]
                classname = classnames.split(' ')[1]
                port_sum = 0
                for c in classname:
                    port_sum *= 10
                    port_sum += key.index(c)
                port = port_sum >> 3
                yield '{}:{}'.format(ip, port)
            except Exception as e:
                print(e)

       
