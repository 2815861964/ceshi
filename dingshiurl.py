import os
import threading
import time
import webbrowser

from selenium import webdriver
from time import ctime
from r_configs import CONFIGS
class urlmanger:
    def __init__(self,config):
        self.urlpath=config['folder_path']
        self.time=config['time']
        self.name=config['name']
        self.urls=self.urls_prase(self.urlpath)
    def sendtochrome(self):
        for url in self.urls:
            webbrowser.open_new_tab(url)
            time.sleep(1)
    def time_to_read(self):
        return self.time == ctime().split()[-2]
    def urls_prase(self,path):
        urls=[]
        for f in os.listdir(path):
            full_path = path+'/'+f
            with open(full_path,'r') as raw_url:
                url = raw_url.read().split('URL=')[-1]
                urls.append(url)
                print(url)
        return urls
    def run(self):
        def _run():
            while True:
                if self.time_to_read():
                    self.sendtochrome()
                    print("111")
                else:
                    print("222")
                time.sleep(0.5)
        t = threading.Thread(target=_run)
        t.daemon=True
        t.start()
        t.join()

manger = [urlmanger(c) for c in CONFIGS]
for m in manger:
    m.run()

