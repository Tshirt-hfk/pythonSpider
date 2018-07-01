import pdfkit, os
from urllib import request, parse
path = os.path.join(os.path.abspath('.'), 'webpage') + '\\'
print(path)
def zhihu_login():
    url = 'https://www.zhihu.com/login/phone_num'
    req = request.Request(url)
    req.add_header(
        'User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
    )
    login_data = parse.urlencode([
        ('phone_num','13717979538'),
        ('password','13866079469'),
        ('_xsrf','8c64809ce35a0ecc7d88cbfd7a338577')
    ])
    with request.urlopen(req,data=login_data.encode('gbk')) as f:
        print(eval(f.read().decode('utf-8'))['msg'])
        return f.headers['Set-Cookie']

def main():
    Cookie = zhihu_login()
    req = request.Request('https://zhuanlan.zhihu.com/p/25785898?group_id=825378309536890880')
    req.add_header(
        'Cookie',Cookie
    )
    req.add_header(
        'User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
    )
    with request.urlopen(req) as f:
        data=f.read()
    with open(path+'1.html', 'wb') as g:
        g.write(data)
    pdfkit.from_file(path+'1.html',path+'out.pdf')

if __name__ == '__main__':
    main()