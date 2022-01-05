import socket
import time

sk = socket.socket(type=socket.SOCK_DGRAM)
qqline_ip_port = ('127.0.0.1', 8081)
qqmsg_ip_port = ('127.0.0.1', 8080)
myqq = '002'
sk.sendto(myqq.encode('utf-8'), qqline_ip_port)    # 将QQ号上传服务器
qqfriends = ['001', '002', '003', '004']
while 1:
    print(myqq + '的qq好友列表：',)
    for i in qqfriends:
        print(i)
    qqfriend = input('请选择聊天好友:').strip()
    if qqfriend == 'bye':
        sk.sendto((myqq + '[>)(<]' + qqfriend).encode('utf-8'), qqline_ip_port)
        break
    if qqfriend in qqfriends:
        while 1:
            # sendmsg = input('我说：')
            # if sendmsg == 'bye':
            #     break
            # sk.sendto((myqq + '[>)(<]' + qqfriend + '[>)(<]' + sendmsg).encode('utf-8'), qqmsg_ip_port)
            recvmsg, addr = sk.recvfrom(1024)
            print()
            print(time.ctime())
            print(qqfriend + '说：', recvmsg.decode('utf-8'))
            print()
sk.close()
