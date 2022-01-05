import socket
import time

sk = socket.socket()
sk.connect(('127.0.0.1', 8080))

while 1:
    sendtime = str(time.ctime())
    sendinfo = input('我说：')
    # sk.send(bytes(sendtime, encoding='utf-8'))
    # sk.send(bytes(sendinfo, encoding='utf-8'))
    sk.send(sendtime.encode('utf-8'))
    sk.send(sendinfo.encode('utf-8'))
    ret = sk.recv(1024).decode(encoding='utf-8')
    if ret == 'bye':
        break
    print()
    print(time.ctime())
    print('他说：', ret)
    print()
sk.close()
