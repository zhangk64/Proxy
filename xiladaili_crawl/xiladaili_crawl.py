#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/5 15:40
# @Author  : m02he
# @File    : xiladaili_crawl.py

import re
import time
import requests

class xiladaili():
    def __init__(self):
        self.file = open("xiladaili_ip.txt", mode='w')
        self.base_url = "http://www.xiladaili.com/gaoni/"
        self.page = 20

    def crawl_ip(self):
        for i in range(1, self.page + 1):
            time.sleep(1) # 请求太频繁会导致503
            try:
                url = self.base_url + str(i)
                print url
                header = {
                    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
                }
                req = requests.get(url, headers=header, timeout=60)
                if req.status_code == 200:
                    result = re.findall(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}:\d{1,5}', req.text)
                    if result:
                        for i in range(len(result)):
                            self.file.write(result[i] + "\n")
                            self.file.flush()
                            print result[i]
            except Exception, e:
                print str(e)
            time.sleep(10)


if __name__ == "__main__":
    test = xiladaili()
    test.crawl_ip()