# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 13:48:59 2018

@author: Prav
"""

from threading import Thread

res=[]
def getStr(name):
    res.append(name)


threads=[]
threads.append(Thread(target=getStr, args=("prav",)))
threads.append(Thread(target=getStr, args=("navya",)))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
print(res)