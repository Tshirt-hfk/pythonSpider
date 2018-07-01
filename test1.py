import queue, os, re
import requests
from bs4 import BeautifulSoup
from threading import Thread
import random

init_url = "https://book.douban.com/tag/?icn=index-nav"
proxy_ip = []
proxy_url = "http://www.xicidaili.com/wt/"

my_headers=[
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",  
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",  
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0"  
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",  
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"
    ]

def getHeader():
    return {"User-Agent": random.choice(my_headers)}

def ipSure():
    try:
        data = requests.get(url=init_url)
        print(data.status_code)
    except:
        return False
    return True


def init_ips():
    for i in range(1,2):
        data = requests.get(url=proxy_url+str(i), headers=getHeader())
        soup = BeautifulSoup(data.text, "lxml")
        trs = soup.select("body > #wrapper > #body > table > tr")
        for tr in trs[1:]:
            td = tr.find_all("td")
            s = "http://"+td[1].text+":"+td[2].text
            if ipSure(s):
                print(s)
                proxy_ip.append(s)

ipSure()