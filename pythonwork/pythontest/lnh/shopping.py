# 函数的方式写注册、登录、退出；为其他页面函数加装饰器，达到一次登录成功后，访问其他菜单不用再输入密码。
from os import mkdir
from os.path import exists, getsize
from functools import wraps
import time

dir = 'txt/shopping'
usersfile = dir + '/users.txt'  # 定义用户密码文件
logsfile = dir + '/logs'        # 定义日志文件
login_succes = 0                # 用户是否登录成功？ 0 失败 1成功
username_succes = ''            # 登录成功的用户名

# 装饰器
def wraper_authen(f):  # 再次判断登录成功后，传入的用户名、密码是否正确。此纯属为练习装饰器。
    @wraps(f)
    def inner(*args):
        authen_success = 0
        with open(usersfile, mode='r', encoding='utf-8') as f_wraper_authen:
            for i in f_wraper_authen:
                if args[0] == i.split()[0] and args[1] == i.split()[1]:
                    authen_success = 1
                    break
        if authen_success == 0:
            print('登录超时，重新登录。')
            my_main()
        ret = f()
        return ret
    return inner

def log(f):
    def inner(*args, **kwargs):
        res = f(*args, **kwargs)
        if login_succes == 1:
            log1 = str(time.asctime()) + '\t' + f.__name__ + '()\t' + username_succes + '\n'
        else:
            log1 = str(time.asctime()) + '\t' + f.__name__ + '()\n'
        with open(logsfile, mode='a', encoding='utf-8') as f_log:
            f_log.write(log1)
        return res
    return inner

# -----------首页-----------


def init():
    if not exists(dir):
        mkdir(dir)
    if not exists(usersfile):
        with open(usersfile, mode='w', encoding='utf-8') as f_init_w:
            f_init_w.write('')
    if not exists(logsfile):
        with open(logsfile, mode='w', encoding='utf-8') as f_init_w:
            f_init_w.write('')

@log
def reg():
    flag_reg = 1
    while flag_reg:
        user_reg = input('注册用户名：').strip()
        if getsize(usersfile) != 0:
            with open(usersfile, mode='r', encoding='utf-8') as f_reg_r:
                for i in f_reg_r:
                    if user_reg == i.split()[0]:
                        print('用户已注册,请重新输入。')
                        continue
                    else:
                        flag_reg = 0
        else:
            flag_reg = 0
    passwd_reg = input('注册密码：').strip()
    with open(usersfile, mode='a', encoding='utf-8') as f_reg_w:
        ins = user_reg + ' ' + passwd_reg + '\n'
        f_reg_w.write(ins)

@log
def login(counts_login):
    '''
    登录模块
    :param counts_login: 登录失败的次数
    :return:
    '''
    global login_succes
    global username_succes
    flag_login = 1
    while flag_login:
        user_login = input('输入用户名(Q返回)：').strip()
        if user_login.upper() == 'Q':
            my_main()
        passwd_login = input('输入密码：').strip()
        with open(usersfile, mode='r', encoding='utf-8') as f_login:
            for i in f_login:
                if user_login == i.split()[0] and passwd_login == i.split()[1]:
                    print('登录成功')
                    login_succes = 1    # 将登录成功标志置为1
                    username_succes = user_login
                    return login_succes, user_login, passwd_login

            if login_succes == 0:
                # nonlocal counts_login
                counts_login -= 1
                if counts_login == 0:
                    print('登录失败次数过多，退出登录')
                    return login_succes, user_login
                print('登录失败,还有{}次机会。'.format(counts_login))


@log
def quit():
    print('退出')
    global flag
    flag = 0


# 用户登录后的页面：-----------------


# 商品模块
@log
def goodsworld(user_login, passwd_login):
    print('欢迎进入{}的商品世界。'.format(user_login))
    flag_goods = 1
    while flag_goods:
        menu_goods = input('选则商品类别：电器（E），手机（P），电脑（C），退出（Q）：').strip()
        if menu_goods.upper() == 'E':
            elec(user_login, passwd_login)
        elif menu_goods.upper() == 'P':
            phone(user_login, passwd_login)
        elif menu_goods.upper() == 'C':
            compu(user_login, passwd_login)
        elif menu_goods.upper() == 'Q':
            break
        else:
            print('输入内容不规范，重新输入')



@log
@wraper_authen
def elec():
    print('elec')

@log
@wraper_authen
def phone():
    print('phone')

@log
@wraper_authen
def compu():
    print('compu')





def my_main():
    init()
    flag = 1
    while flag:
        inp1 = input('menu:注册(R),登录(L),退出(Q):').strip()
        if inp1.upper() == 'Q':
            quit()
        elif inp1.upper() == 'L':
            res = login(3)
            if res[0] == 1:  # 如果登录成功，则进入userworld菜单
                print('==================')
                goodsworld(*res[1:3]) # 参数以user_login, passwd_login两个位置参数的形式传入userworld()函数
        elif inp1.upper() == 'R':
            reg()
        else:
            print('输入有误，重新输入')
            continue


my_main()