#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/5 9:19
# @Author  : m02he
# @File    : check_proxy_ip.py

# 多线程检测代理ip是否有效

import threading
import Queue
import requests

class Check_ip():
    def __init__(self):
        self.qip = Queue.Queue()
        self.thread_num = 50
        self.lock = threading.Lock()

    def get_ip(self):
        for line in open("ip.txt"):
            ip = line.strip()
            self.qip.put(ip)
        print "======================"

    def verify(self):
        self.get_ip()
        ths = []
        for i in range(self.thread_num):
            th = threading.Thread(target=self.check())
            th.start()
            ths.append(th)
        for th in ths:
            th.join()

    def check(self):
        while True:
            # self.lock.acquire()
            if self.qip.empty():
                # self.lock.release()
                break
            ip = self.qip.get()
            try:
                proxy = {
                    "http": ip,
                    "https": ip
                }
                url = "http://icanhazip.com/"
                req = requests.get(url, proxies=proxy, timeout=60)
                if req.status_code == 200:
                    print ip
            except Exception, e:
                print ".",
                pass
            # self.lock.release()
        # print threading.current_thread().getName()

if __name__ == "__main__":
    test = Check_ip()
    test.verify()