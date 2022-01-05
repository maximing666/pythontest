import os
from functools import wraps


managers_f_dir = 'txt'
managers_f = managers_f_dir + '/managers'
counts_login = 3
login_success = 0


def wrapper_login(func):
    @wraps(func)
    def inner(*args, **kwargs):
        global login_success
        if not os.path.exists(managers_f_dir):
            os.mkdir(managers_f_dir)  # 创建文件目录
        if not os.path.exists(managers_f):
            with open(managers_f, mode='w', encoding='utf-8') as f_users:  # 创建管理员列表
                f_users.write('')
        menu = input('登录/L,退出/Q: ').strip()
        if menu.upper() == 'Q':
            exit()
        elif menu.upper() == 'L':
            flag_login = 1
            while flag_login:
                user_login = input('输入用户名：').strip()
                passwd_login = input('输入密码：').strip()
                with open(managers_f, mode='r', encoding='utf-8') as f_login:
                    for i in f_login:
                        if user_login == i.split()[0] and passwd_login == i.split()[1]:
                            print('登录成功')
                            login_success = 1
                            flag_login = 0
                            ret = func(*args, **kwargs)
                            return ret
                    if login_success == 0:
                        # nonlocal counts_login
                        global counts_login
                        counts_login -= 1
                        if counts_login == 0:
                            print('登录失败次数过多，退出登录')
                            exit()
                        print('登录失败,还有{}次机会。'.format(counts_login))

    return inner


def where_sql(input_sql_list, employs_d):
    """
    执行where部分的运算
    :param input_sql_list:输入sql
    :param employs_d:员工表字典
    :return: 运算结果ID的列表
    """
    where_index = input_sql_list.index('where')              # 获取where关键字的索引
    where_content = ''.join(input_sql_list[where_index+2:])  # 获取where中的运算符及以后部分
    sign = ''.join(input_sql_list[where_index+2])            # 获取where部分中的运算符号
    print('where_content:', where_content)
    result_list = []                                         # where部分运算后得到的数据id
    for i in list(employs_d.values())[1:]:
        if i != {'id': ''}:
            d_zhi = i[input_sql_list[where_index + 1]]
            sql_zhi = input_sql_list[where_index + 3]
            if sql_zhi.find('\'') >= 0:                         # 去除where部分中的引号。这关系到以后的判断，如'sdf' == "'sdf'" 结果是False
                sql_zhi = sql_zhi.replace('\'', '')
            elif sql_zhi.find('\"') >= 0:
                sql_zhi = sql_zhi.replace('\"', '')
            if sign == '=':  # 当where部分运算=时
                if d_zhi == sql_zhi:
                    result_list.append(i['id'])
            elif sign.lower() == 'like':   # 当where部分运算 like 时
                if d_zhi.find(sql_zhi) >= 0:
                    result_list.append(i['id'])
            else:                                                    # 当where部分运算其他运算符（<,>） 时
                if eval(str(d_zhi) + where_content):
                    result_list.append(i['id'])
    return result_list


@wrapper_login
def e_to_dict(efile):
    """
    将员工表employs数据转换为字典数据，例如{1:{'id':1,'name':'Alex','age':22,'phone:'13651054608','job':'IT'}}
    :param efile: 员工表的路径/文件名，例如'txt/employs'
    :return:返回整个员工表数据大字典
    """
    e_dict = {}
    rownum = '0'
    with open(efile, mode='r', encoding='utf-8') as efile_r:
        e_menu_list = efile_r.readline().split(',')   # 表头
        efile_r.seek(0)                         # 修改光标至文件起始位置
        for i in efile_r:
            efile_row = i.split(',')            # 员工表每行数据列表
            if efile_row[0] == '\n':
                continue
            if efile_row[0] != 'id':
                rownum = efile_row[0]
            e_dict[rownum] = {}
            for m, n in zip(e_menu_list, efile_row):  # 同时遍历两个列表用zip函数
                e_dict[str(rownum)][m.strip()] = n.strip()
        efile_r.seek(0, 2)
    return e_dict


def sql_to_list(input_sql):
    """
    分割sql语句为list
    :param input_sql:输入的sql语句
    :return: sql语句的list形式
    """
    input_sql_list = input_sql.split(' ')  # 按空格分割
    for i in [',', '>', '<', '=', 'like', 'LIKE', '(', ')']:
        for j in input_sql_list:
            if j.find(i) >= 0 and j != i:
                j_index = input_sql_list.index(j)  # input_sql_list中j元素的索引
                j_list = j.strip().split(i)
                n = 1
                j_list_len = len(j_list)
                for m in range(j_list_len-1):    # 将特殊符号添加到j_list列表中
                    j_list.insert(n, i.strip())
                    n += 2
                while '' in j_list:     # 去除j_list中的空值''
                    j_list.remove('')
                while ',' in j_list:     # 去除j_list中的逗号','
                    j_list.remove(',')
                while '\'' in j_list:     # 去除j_list中的单引号'\''
                    j_list.remove('\'')
                while '(' in j_list:     # 去除j_list中的左括号'（'
                    j_list.remove('(')
                while ')' in j_list:     # 去除j_list中的右括号'）'
                    j_list.remove(')')
                input_sql_list.remove(j)      # 在原列表input_sql_list中删除j
                for x in j_list:                    # 将input_sql_list列表元素中含关键字的，导入列表
                    input_sql_list.insert(j_index, x)
                    j_index += 1
    while '' in input_sql_list:  # 去除j_list中的空值''
        input_sql_list.remove('')
    return input_sql_list


def insert(input_sql_list, employs_d, employs_f):
    """
    新增数据
    示例：insert into (name,age,phone,job) values (nlili,25,1333295322,IT)
    :param employs_d:
    :param input_sql_list:
    :return:
    """
    print('insert语句')
    values_index = input_sql_list.index('values')
    # rowid_new = int(list(employs_d.values())[-1]['id']) + 1   # 新行行号ID
    rowid_new = str(int(list(employs_d.keys())[-1]) + 1)
    key_list = input_sql_list[2:values_index]    # 新增key列表
    v_list = input_sql_list[values_index + 1:]   # 新增value值
    print(key_list, v_list)
    tmp_d = {'id': str(rowid_new)}                                   # 临时字典，存放员工数据
    for i, j in zip(key_list, v_list):
        tmp_d[i] = j
    employs_d[rowid_new] = tmp_d                  # 添加新数据到employs_d字典中
    row_new = ','.join(list(list(employs_d.values())[-1].values()))  # 新增数据
    with open(employs_f, mode='a', encoding='utf-8') as employs_f_insert:
        employs_f_insert.seek(0, 2)
        employs_f_insert.write(row_new + '\n')


def delete(input_sql_list, employs_d, employs_f):
    """
    删除数据，示例：delete where name='Alex'
    :param employs_d:
    :param input_sql_list:
    :return:
    """
    print('delete语句')
    ret_list = where_sql(input_sql_list, employs_d)
    print(ret_list)
    for i in ret_list:
        employs_d[i].clear()      # 此处是清空每行的列表，不删除
    with open(employs_f, mode='w+', encoding='utf-8') as employs_f_d:
        for j in employs_d.values():
            if j == {}:            # 如果j为空，则不写入文本。及删除的空行不写入文本。
                continue
            employs_f_d.write(','.join(j.values()) + '\n')


def update(input_sql_list, employs_d, employs_f):
    """
    更新。# 格式：update set <列名=更新值> [where <更新条件>  例如：update set age='18' where name='Alex'
    :param input_sql_list:
    :param employs_d:
    :param employs_f:
    :return:
    """
    print('update语句')
    ret_list = where_sql(input_sql_list, employs_d)
    sql_zhi = input_sql_list[4]
    for i in ret_list:
        if sql_zhi.find('\'') >= 0:
            sql_zhi = sql_zhi.replace('\'', '')
        employs_d[i][input_sql_list[2]] = sql_zhi
    with open(employs_f, mode='w+', encoding='utf-8') as employs_f_d:
        for j in employs_d.values():
            if j == {}:            # 如果j为空，则不写入文本。及删除的空行不写入文本。
                continue
            employs_f_d.write(','.join(j.values()) + '\n')


def select(input_sql_list, employs_d):
    """ 例句：
    select name, age where age>22
    select * where job=IT
    select * where phone like 133
    """
    where_index = input_sql_list.index('where')
    ret_list = where_sql(input_sql_list, employs_d)
    if ''.join(input_sql_list[1:where_index]) == '*':
        for i in ret_list:
            print(list(employs_d[i].values()))
    else:
        for i in ret_list:
            for j in input_sql_list[1:where_index]:
                print(employs_d[i][j], end=' ')
            print('')


def exe_sql(input_sql_list, employs_d, employs_f):
    """
    sql函数,使用于增删改查
    :param employs_d: 员工表字典
    :param input_sql: 输入的sql语句分割为list的形式
    :return: sql的结果
    """
    if input_sql_list[0].lower() == 'insert':
        insert(input_sql_list, employs_d, employs_f)
    elif input_sql_list[0].lower() == 'delete':
        delete(input_sql_list, employs_d, employs_f)
    elif input_sql_list[0].lower() == 'update':
        update(input_sql_list, employs_d, employs_f)
    elif input_sql_list[0].lower() == 'select':
        select(input_sql_list, employs_d)
    else:
        print('sql语句不规范。')


def main(employs_f):
    # login_success = login.login('txt/', 'txt/managers', 3)
    # if login_success[0] == 1:
    global login_success
    while 1:
        if login_success != 1:
            employs_d = e_to_dict(employs_f)  # 调用读取员工表函数
        input_sql = input('sql>>>').strip()  # 输入sql语句
        input_sql_list = sql_to_list(input_sql)  # 将sql语句解析为list列表
        print('input_sql_list', input_sql_list)
        exe_sql(input_sql_list, employs_d, employs_f)                            # 执行sql语句


employs_f = 'txt/employs'
main(employs_f)   # 调用主函数，参数为员工表路径
