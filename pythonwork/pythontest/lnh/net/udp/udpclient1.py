import socket
import time

sk = socket.socket(type=socket.SOCK_DGRAM)
ip_port = ('127.0.0.1', 8080)
while 1:
    sendmsg = input('我说：')
    sk.sendto(sendmsg.encode('utf-8'), ip_port)
    recvmsg, addr = sk.recvfrom(1024)
    print()
    print(time.ctime())
    print('server说：', recvmsg.decode('utf-8'))
    print()
