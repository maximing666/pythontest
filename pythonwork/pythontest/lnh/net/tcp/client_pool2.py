import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 8090))
while 1:
    msg = sk.recv(1024).decode('utf-8')
    print(msg)
    msgi = input('>>>').encode('utf-8')
    if msgi == 'q': break
    sk.send(msgi)
sk.close()