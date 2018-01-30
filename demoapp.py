#-*-coding: utf-8-*-
from flask import Flask
from flask import render_template #jinja2
from flask import request
import urllib2,urllib

app = Flask(__name__)

#向百度发起请求（爬虫模块）
def getHtml(wd,pn):
    #百度会判断是用机器还是浏览器访问的
    #添加头信息，告诉百度我使用浏览器访问的
    req = urllib2.Request('https://www.baidu.com/s?wd=%s&pn=%s' % (wd,pn))
    req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')
    return urllib2.urlopen(req).read()

#装饰器
@app.route('/')  #定义路由
def index():
    return render_template('index.html')
    #return render_template('demo1.html', name = 'aaa')
    #return render_template('demo1.html', names = ['qiangzi','xiaoming'])

@app.route('/s')
def search():
    if request.method == 'GET':
        wd = request.args.get('wd')
        wd = urllib.quote(wd.encode('utf-8')) #urllib.quote只能解码utf-8,所以先编码
        pn = request.args.get('pn')
        return getHtml(wd,pn)
    else:
        return None
  
if __name__ == '__main__':
    app.debug = True  #开启调试模式
    app.run(host = '0.0.0.0', port = 5000) #所有IP可访问，指定端口8000