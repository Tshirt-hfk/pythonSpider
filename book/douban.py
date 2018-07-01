import requests
from bs4 import BeautifulSoup
from dbConnector import DBConnector
from threading import Thread
from proxyIP import ProxyIP
import numpy as np
from headers import getHeaders


url = []
init_url = "https://book.douban.com/tag/?icn=index-nav"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
pi = ProxyIP(init_url)

#def zhihu_login():
#    login_url = 'http://accounts.douban.com/login'
#    login_data = {
 #   		'redir':'http://www.douban.com',
#	        'form_email':'13717979538',
#			'form_password': '13866079469',
#			'remember':'on'
 #   	}
  #  data = requests.post(login_url, headers=headers, data=login_data)
 #   print(data.cookies)
  #  return data.cookies
#cookies = zhihu_login()

def init_urls():
	data = requests.get(url=init_url, headers=getHeaders(), proxies=pi.getProxyIP())
	soup = BeautifulSoup(data.text, "lxml")
	print(data.text)
	tags = soup.select("#content > div > div.article > div > div > table > tbody > tr > td > a")
	temp_url = "https://book.douban.com/tag/"
	print(tags)
	for tag in tags:
		tag = tag.get_text()
		url.append(temp_url+tag)

class Mythread(Thread):
	def __init__(self, init_url):
		Thread.__init__(self)
		self.db = DBConnector()
		self.category_url = init_url

	def storeMessage(self, book_url):
		nurl = pi.getProxyIP()
		data = requests.get(book_url, headers=getHeaders(), proxies=nurl)
		try:
			soup = BeautifulSoup(data.text, "lxml")
			tags = soup.select("body > #wrapper")
			name = tags[0].select("h1 > span")[0].text
			info = tags[0].select("#content > div > div.article > div.indent > div.subjectwrap > div.subject > #info")
			author = info[0].a.text.replace(" ","").replace("\n","")
			if self.db.insert(book_url, name, author):
				print(name, "get!!!")
		except:
			if data.status_code != 200:
				print(str(data.status_code)+":"+ nurl.get("http"))
				pi.ipHandler(nurl)
			self.storeMessage(book_url)

	def run(self):
		s = 0
		sum = 0
		while True:
			n_url = self.category_url+"?start="+str(s)+"&type=T"
			s += 20
			data = requests.get(n_url, headers=getHeaders(), proxies=pi.getProxyIP())
			soup = BeautifulSoup(data.text, "lxml")
			tags = soup.select("#subject_list > ul > li > div.pic > a")
			if len(tags) == 0:
				break
			for tag in tags:
				book_url = tag["href"]
				sum += 1
				if not self.db.isExisted(book_url):
					self.storeMessage(book_url)
		print(self.category_url, "%d本书 all get!!!" % sum)
		self.db.close()

init_urls()	
print(url)
threads = []
for u in url:
	t = Mythread(u)
	t.start()
	threads.append(t)