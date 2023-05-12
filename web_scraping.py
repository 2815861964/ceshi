import requests
from bs4 import BeautifulSoup
import time
from multiprocessing.dummy import Pool
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}
ls=[]
def sc(start_num):
    response = requests.get(f"https://movie.douban.com/top250?start={start_num}", headers=headers)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    all_titles = soup.findAll("span", attrs={"class": "title"})
    for title in all_titles:
        title_string = title.string
        if "/" not in title_string:
            print(title_string)
            ls.append(title_string)
start = time.perf_counter()
pool = Pool(5)
ls = [x for x in range(0,250,25)]
pool.map(sc,ls)
end = time.perf_counter()
print(end-start)
for i in ls:
    print(i)