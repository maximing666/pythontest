import requests
r=requests.get('https://www.douban.com/')
print(r.status_code)
print('----------------')
#print(r.text)
r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
print(r.url)
#requests自动检查编码
print(r.encoding)
#获得bytes对象
print(r.content)
#传入HTTP Header
r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
print(r.text)
#获取响应头
print(r.headers)
print(r.headers['Content-Type'])
#获取cookie
#print(r.cookies('ts'))