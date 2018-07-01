# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
from dbConnector import DBConnector
import numpy as np
import time

url = []
init_url = "https://book.douban.com/tag/?icn=index-nav"
headers = {'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20"}
db = DBConnector()

def zhihu_login():
    login_url = 'http://accounts.douban.com/login'
    login_data = {
    		'redir':'http://www.douban.com',
	        'form_email':'13717979538',
			'form_password': '13866079469',
			'remember':'on'
    	}
    data = requests.post(login_url, headers=headers, data=login_data)
    print(data.cookies)
    return data.cookies

cookies = zhihu_login()

def init_urls():
	time.sleep(np.random.rand()*5)
	data = requests.get(url=init_url, headers=headers, cookies=cookies)
	print(data.status_code)
	soup = BeautifulSoup(data.text, "lxml")
	tags = soup.select("#content > div > div.article > div > div > table > tbody > tr > td > a")
	temp_url = "https://book.douban.com/tag/"
	for tag in tags:
		tag = tag.get_text()
		url.append(temp_url+tag)

def storeMessage(book_url):
	time.sleep(np.random.rand()*5)
	data = requests.get(book_url, headers=headers, cookies=cookies)
	soup = BeautifulSoup(data.text, "lxml")
	tags = soup.select("body > #wrapper")
	try:
		name = tags[0].select("h1 > span")[0].text
		info = tags[0].select("#content > div > div.article > div.indent > div.subjectwrap > div.subject > #info")
		author = info[0].a.text.replace(" ","").replace("\n","")
		if db.insert(book_url, name, author):
			print(name, "get!!!")
	except:
		print(book_url)

def get_book_url(category_url):
	print(category_url, "start!!!")
	s = 0
	while True:
		n_url = category_url+"?start="+str(s)+"&type=T"
		print(s)
		s += 20
		time.sleep(np.random.rand()*5)
		data = requests.get(n_url, headers=headers, cookies=cookies)
		soup = BeautifulSoup(data.text, "lxml")
		tags = soup.select("#subject_list > ul > li > div.pic > a")
		if len(tags) == 0:
			break
		for tag in tags:
			book_url = tag["href"]
			if not db.isExisted(book_url):
				storeMessage(book_url)
			else:
				print(book_url, "have gotten!!!")
	print(category_url, "all get!!!")

init_urls()
print(url)
for u in url[13:]:
	get_book_url(u)

#storeMessage("https://book.douban.com/subject/1082577/")
db.close()