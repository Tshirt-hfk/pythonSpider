# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
from dbConnector import DBConnector
import numpy as np
import time
import re

headers = {'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20"}
regex1 = re.compile(r'、([\u4e00-\u9fa5|，；。？“”：]*)')
regex2 = re.compile(r'——([\u4e00-\u9fa5]*)')

def open_url(db, m_url, title):
	data = requests.get(m_url, headers=headers)
	soup = BeautifulSoup(data.content, "lxml")
	tags = soup.select("body > #container > #p_left > .viewbox > .content > p")
	for x in tags[::2]:
		if (regex2.findall(x.text)):
			db.insert(content=regex1.findall(x.text)[0], author=regex2.findall(x.text)[0], title=title)

if __name__ == "__main__":
	db = DBConnector()
	while True:
		url=input("url(输入NO结束):")
		if url=="NO":
			break
		title = input("title:")
		open_url(db, url, title)
	db.close()
	