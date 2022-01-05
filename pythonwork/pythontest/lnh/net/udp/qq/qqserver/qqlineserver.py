import socket
import time

sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1', 8081))
qqlist={}
while 1:
    msg, addr = sk.recvfrom(1024)
    ret = msg.decode('utf-8')
    qqlist[ret] = addr
    print(time.ctime(), 'QQ号:'+ret+'  上线了.')
    print(qqlist)
    print()

