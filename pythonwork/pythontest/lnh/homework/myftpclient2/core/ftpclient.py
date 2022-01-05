from os.path import getsize
import socket
import json
import struct
import time
import hashlib
from conf.config import *
from core.hashlibfile import *

class ftpclient:

    def sendfile(self):
        sk = socket.socket()
        sk.connect((server_ip, server_port))
        filepath = input('输入上传文件的全目录:').strip()
        filename = input('输入上传文件名称:').strip()
        filesize = getsize(filepath + '\\' + filename)
        filefull = filepath + '\\' + filename
        print(filefull)
        f_hash = hashlibfile(filefull)
        file_md5 = f_hash.hash()
        starttime = time.time()
        head = {'filepath': filepath,
                      'filename': filename,
                      'filesize': filesize,
                      'filemd5': file_md5
                      }
        print(file_md5)
        head_j = json.dumps(head).encode('utf-8')
        head_j_len = len(head_j)
        head_j_len_struct = struct.pack('i', head_j_len)
        sk.send(head_j_len_struct)
        sk.send(head_j)
        exist_flag = sk.recv(7).decode('utf-8')
        if exist_flag == 'unexist':
            filesize_total = filesize
            filenow = 0
            with open(filefull, mode='rb') as f:
                while filesize > 0:
                    fr = f.read(buffer)
                    sk.send(fr)
                    filesize -= buffer
                    filenow = filesize_total - filesize
                    persent = "%.0f%%" % (filenow*100/filesize_total)
                    print('\r' + persent + '- '*(int(persent.split('%')[0])//5), end='', flush=True)
            endtime = time.time()
            usetime = int(endtime - starttime)
            print('\r传输完成,用时%s秒.' % usetime)
        else:
            print('\r文件已经存在')
        print()

    def recvfile(self):
        pass
