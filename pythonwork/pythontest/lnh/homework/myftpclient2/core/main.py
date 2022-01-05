from core.ftpclient import *

def main():
    menu = {'上传文件': 'sendfile',
            '下载文件': 'recvfile'}
    menu_l = list(enumerate(menu, 1))
    print(menu_l)
    print('\033[33m欢迎使用MyFtp服务\033[0m')
    while 1:
        for i, j in menu_l:
            print(i, j)
        try:
            input_n = int(input('请输入序号：').strip())
        except ValueError:
            print('输入格式有误')
        ftp_c = ftpclient()
        func = getattr(ftp_c, menu[menu_l[input_n - 1][1]])
        func()
