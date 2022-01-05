import json
import struct
import socket
from ../conf.config import *
from os import getcwd

class ftpserver:
    def ftpserver_recv(self):
        sk = socket.socket()
        sk.bind(server_ip, server_port)
        sk.listen()
        
        while 1:
            conn, addr = sk.accept()
            head_len = conn.recv(4)
            head_len = struct.unpack('i', head_len)
            head_json = conn.recv(head_len)
            head = json.loads(head_json)
            file_len = head[filesize]
            file = conn.recv(file_len)
            file_name = head[filename]
            with open('../db/'+file_name, mode='wb') as f:
                f.write(file)


