import socket,threading,time

#创建一个基于IPV4和TCP协议的SOCKET
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#监听端口
s.bind(('127.0.0.1',9999))
#连接最大数
s.listen(5)
print('Waiting for connection...')
#通过永久循环来监听客户端连接
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome.')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello,%s' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)


while True:
    #接受一个新连接
    sock,addr = s.accept()
    print(sock)
    print(addr)
    #创建新线程来处理TCP连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
    print(t.name)





