print('-------------datetime')
from datetime import datetime
print('现在时间：',datetime.now())

import time
print('现在时间：',time.ctime())

dt=datetime(2015,10,31,12,00)
print('指定时间：',dt)
ts=dt.timestamp()
print('datetime转为timestamp:',ts)
dt1=datetime.fromtimestamp(ts)
dt2=datetime.utcfromtimestamp(ts)
print('timestamp转为datetime(本地时区时间):',dt1)
print('timestamp转为datetime(标准时区时间):',dt2)

cday=datetime.strptime('2015-6-1 18:19:58','%Y-%m-%d %H:%M:%S')
print('str转datetime:',cday,'  ',type(cday))

now=datetime.now()
s=now.strftime('%Y-%m-%d %H:%M:%S')
print('datetime转str:',s,'  ',type(s))

print('------------OrderedDict')
from collections import OrderedDict
od=OrderedDict([('a',1),('c',3),('b',2)])
print(od)
od1=dict([('a',1),('c',3),('b',2)])
print(od1)


print('------------chainmap')
from collections import ChainMap
import os, argparse

# 构造缺省参数:
defaults = {
    'color': 'red',
    'user': 'guest'
}

# 构造命令行参数:
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = { k: v for k, v in vars(namespace).items() if v }

# 组合成ChainMap:
combined = ChainMap(command_line_args, os.environ, defaults)

# 打印参数:
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])

print('------------------collections.counter')
from collections import Counter
a='hellowold'
c=Counter()
for i in a:
    c[i]=c[i]+1
print(c)


print('--------------------hmac')
import hmac
message='Hello,world!中国'.encode('utf-8')
key=b'secret'
h=hmac.new(key,message,digestmod='md5')
print(h.hexdigest())


print('------------------itertools.count()')
import itertools
na=itertools.count(1)
ns=itertools.takewhile(lambda x:x<=10,na)
print(list(ns))

'''
print('--------------------@closing')
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)
'''

print('--------------------urllib')
from urllib import request
with request.urlopen('https://cloudcard.cecurs.com:38080/BaodingHCECloudService/login') as f:
    data=f.read()
    print('status:',f.status,f.reason)

    for k,v in f.getheaders():
        print('%s:%s' % (k,v))
   # print('data:',data.decode('utf-8'))

print('-----------------------urllib:模拟iPhone 6去请求')
from urllib import request
req = request.Request('https://cloudcard.cecurs.com:38080/BaodingHCECloudService/login')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))


print('------------------------post登录微博')
from urllib import request, parse

print('Login to weibo.cn...')
email = input('Email: ')
passwd = input('Password: ')
login_data = parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))







