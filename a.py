import queue, os, re
from urllib import request

url_queue = queue.Queue()
init_url = r"http://big.bilibili.com/site/big.html"
visited = set()
path = os.path.join(os.path.abspath('.'), 'webpage') + '\\'
regex = re.compile(r'href="(.*?)"')

def main():
	url_queue.put(init_url)
	visited.add(init_url)
	i=1
	while True:
		if not url_queue.empty():
			url=url_queue.get()
			print('urlopen%d:'%i,url )
			try:
				data=request.urlopen(url).read()
			except:
				continue
			with open(path+'%d'%i+'.html', 'wb') as f:
				f.write(data)
			i=i+1
			data=data.decode('utf-8')
			arr=regex.findall(data)
			for str in arr:
				if str[0:2]=='//':
					str='http:'+str
				elif str[0]=='/':
					str=init_url+str[1:]
				else:
					continue
				if str[-5:]=='.html':
					if not (visited & set([str])):
						url_queue.put(str)
						visited.add(str)
						print(str)
		else:
			break
			
if __name__ == '__main__':
	main()