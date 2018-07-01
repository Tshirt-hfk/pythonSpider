import pdfkit, os
from urllib import request, parse
path = os.path.join(os.path.abspath('.'), 'webpage') + '\\'

def zhihu_login():
    url = 'http://localhost:8080/TomcatTest/test'
    req = request.Request(url)
    req.add_header(
        'User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
    )
    login_data = parse.urlencode([
        ('firstName','方'),
        ('nameNum','3'),
        ('gender','M')
    ])
    with request.urlopen(req,data=login_data.encode('utf-8')) as f:
        print(eval(f.read().decode('utf-8'))['msg'])
        print(f.body)

def main():
    zhihu_login()

if __name__ == '__main__':
    main()