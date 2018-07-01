from threading import Thread
from bs4 import BeautifulSoup
from headers import getHeaders
import random, threading, time, requests, sys

class ProxyIP(object):
	def __init__(self, filterUrl):
		self.__proxyIpPool = []
		self.__proxyUrl = "http://tvp.daxiangdaili.com/ip/?tid=559736697125509&num=1000"
		self.__filterUrl = filterUrl
		self.__a = 0
		self.__storeIP()

	def getProxyIP(self):
		proxy_ip = random.choice(self.__proxyIpPool)
		return {"http" : proxy_ip}

	def ipHandler(self, ip):
		self.__proxyIpPool.pop(ip)

	def __proxyIpFilter(self, ip):
		try:
			data = requests.get(url=self.__filterUrl, headers=getHeaders(), proxies={"http" : ip})
			print(data.status_code, ":", ip)
			if data.status_code != 200:
				return False
		except:
			return False
		return True

	def __addIP(self, ip):
		if self.__proxyIpFilter(ip):
			self.__proxyIpPool.append(ip)


	def __storeIP(self):
		with open("ips.txt") as f:
			data = f.read()
			ips = data.split("\n")
		for ip in ips:
			print(ip)
			self.__addIP("http:"+ip.strip())
		print("get proxyIP:",len(self.__proxyIpPool))