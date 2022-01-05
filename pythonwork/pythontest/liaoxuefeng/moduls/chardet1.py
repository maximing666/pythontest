import chardet
#检测编码
print(chardet.detect(b'hello,world'))
#检测GBK编码的中文
data='离离原上草，一岁一枯荣'.encode('gbk')
print(chardet.detect(data))
print(data.decode('gbk'))
#检测utf-8编码的中文
data='离离原上草，一岁一枯荣'.encode('utf-8')
print(chardet.detect(data))
print(data.decode('utf-8'))
#检测日文
data = '最新の主要ニュース'.encode('euc-jp')
print(chardet.detect(data))


