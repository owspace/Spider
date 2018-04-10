from urllib import request
from http import cookiejar
import http


url = 'http://www.baidu.com'

print('方法1:直接请求')

response1 = request.urlopen(url)

print(response1.getcode()) # 状态码
print(len(response1.read())) # 网页内容长度


print('')
print('方法2：Request')

req = request.Request(url)

# 把爬虫伪装成了 Mozilla 浏览器
req.add_header('User-Agent','Mozilla/5.0')

response2 = request.urlopen(req)

print(response2.getcode())
print(len(response2.read()))

print('')
print('方法3：增加 cookie 处理 ')

# 创建一个 cookie 容器
cj = http.cookiejar.CookieJar()

# 创建一个 opener。以容器 cj 作为参数创建一个 handler，作为 opener 的参数
opener = request.build_opener(request.HTTPCookieProcessor(cj))

# 给 request 安装 opener。这时 request 有了cookie处理的增强能力。
request.install_opener(opener)

response3 = request.urlopen(url)

print(response3.getcode())
print(cj)
print(response3.read())
