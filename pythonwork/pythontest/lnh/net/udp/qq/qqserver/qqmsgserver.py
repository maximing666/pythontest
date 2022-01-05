import socket
import time

sk = socket.socket(type = socket.SOCK_DGRAM)
sk.bind(('127.0.0.1', 8080))

while 1:
    msg, addr = sk.recvfrom(1024)
    ret = msg.decode('utf-8')
    print(time.ctime())
    print(str(addr) + '说：', ret)
    print()
    sendmsg = input('我对'+str(addr) + '说：')
    sk.sendto(sendmsg.encode('utf-8'), addr)
    print()
