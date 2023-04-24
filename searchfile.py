import os
import time
from multiprocessing.dummy import Pool

path = input("请输入文件夹地址")
searchedfile = input("请输入名称")
files = os.walk(path)
for root,d,list1 in files:
    for file in list1:
        if searchedfile in file and file.endswith(".mp4"):
            print(f"找到了{file}路径为{root}\n")