import os
import shutil

path = input("文件路径")
files = os.listdir(path)
for f in files:
    if not os.path.exists(f"{path}/{f.split('.')[-1]}"):
        os.mkdir(f"{path}/{f.split('.')[-1]}")
        shutil.move(f"{path}/{f}", f"{path}/{f.split('.')[-1]}")
    else:
        shutil.move(f"{path}/{f}",f"{path}/{f.split('.')[-1]}")