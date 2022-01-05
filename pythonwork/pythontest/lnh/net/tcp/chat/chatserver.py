import socket
import time

sk = socket.socket()
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sk.bind(('127.0.0.1', 8080))
sk.listen()
conn, addr = sk.accept()
while 1:
    rettime = conn.recv(1024).decode(encoding='utf-8')
    print(rettime)
    ret = conn.recv(1024).decode(encoding='utf-8')
    if ret == 'bye':
        break
    print('他说:', ret)
    print()
    sendinfo = input('我说:')
    # conn.send(bytes(sendinfo, encoding='utf-8'))
    conn.send(sendinfo.encode('utf-8'))
    print()

conn.close()
sk.close()
