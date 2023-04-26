import os
import filecmp
import time
from multiprocessing.dummy import Pool

alllist = []
path = input("请输入文件夹地址")
files = os.walk(path)
for root,d,list1 in files:
    for file in list1:
         alllist.append(f"{root}/{file}")
for x in alllist:
    for y in alllist:
        if x!=y and os.path.exists(x) and os.path.exists(y):
            if filecmp.cmp(x,y):
                os.remove(y)
                print(f"重复文件{y}已删除")