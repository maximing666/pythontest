import socket,ssl

#访问https网址
#创建socket
s=ssl.wrap_socket(socket.socket())
#建立连接
s.connect(('www.sina.com.cn',443))
#发送数据
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

'''
#访问http网址。如果该http网址做了重定向到https,则需要用访问https的方式。
#创建socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立连接
s.connect(('www.cecurs.com',80))
#发送数据
s.send(b'GET / HTTP/1.1\r\nHost: www.cecurs.com\r\nConnection: close\r\n\r\n')
'''

#接收数据
buffer=[]
while True:
    #每次最多接收1K字节
    d=s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data=b''.join(buffer)
#关闭连接
s.close()

header,html = data.split(b'\r\n\r\n',1)
#打印http头信息
print(header.decode('utf-8'))
#把接收的数据写入文件
with open('d:\sina.html','wb') as f:
    f.write(html)















