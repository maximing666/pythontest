# import os
#
#
# def read_g(file):
#     if not os.path.exists(file):
#         with open(file, mode='w', encoding='utf-8') as f:
#             f.write('')
#     if os.path.getsize(file):
#         input_m = input('输入读取文件方式：按行/L,按字符/S:').strip()
#         if input_m.upper() == 'L':
#             with open(file, mode='r', encoding='utf-8') as f:
#                 iter1 = f.__iter__()
#                 for j in iter1:
#                     ret = '***' + j.strip()
#                     yield ret
#
#         elif input_m.upper() == 'S':
#             with open(file, mode='r', encoding='utf-8') as f:
#                 while 1:
#                     str = f.read(10)
#                     ret = '***' + str
#                     yield ret
#         else:
#             print('输入格式错误。')
#     else:
#         print('读取文件为空')
#
#
# ret = read_g('txt/read_g.txt')
# print(ret)
# print(ret.__next__())


# 传一个数后计算平均值
# def generator():
#     sum = 0
#     count = 0
#     avg = 0
#     while 1:
#         num = yield avg
#         sum += num
#         count += 1
#         avg = sum/count
#         print(avg)
#
#
# g = generator()
# g.__next__()
# g.send(10)
# g.send(20)


# def demo():
#     for i in range(4):
#         yield i
#
# g=demo()
#
# g1=(i for i in g)
# g2=(i for i in g1)
#
#
# print(list(g1))
# print(list(g2))



# a = 'abcdefg'
# b = '1234567'
# for i, j in zip(a, b):
#     print(i + ' ' + j)


# g = (i*i for i in range(10))
# g1 = (i for i in g)
# for i in g1:
#     print(i)


# names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'], ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
# # for i in range(len(names)):
# #     for j in names[i]:
# #         j_index = j.find('e')
# #         if j_index >= 0:
# #             j2 = j[j_index + 1:]
# #             j_index2 = j2.find('e')
# #             if j_index2 >= 0:
# #                 print('---', j)
#
# print([j for i in names for j in i if j.count('e') >= 2])
#
#
# # 合并大小写对应的value值，将k统一成小写
# d = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
# d_new = {k.lower(): d.get(k.lower(), 0) + d.get(k.upper(), 0) for k in d}
# print(d_new)


# def add(n,i):
#     return n+i
#
# def test():
#     for i in range(4):
#         yield i
#
# g=test()
# for n in [1,10]:
#     g=(add(n,i) for i in g)
#
# print(list(g))

# import os
# # 遍历目录及文件
# n = 0
# for i in os.walk('D:\gitlab'):
#     n += 1
#     if n < 5:
#         # print(i)
#         for j in i[2]:
#             if '.sample' in j:
#                 print(i[0] + '\\' + j)
#     else:
#         break

# t = __import__('time')
# print(type(t))

# import time
#
#
# def progress_bar():
#     for i in range(0, 101):
#         time.sleep(0.2)
#         print('\r' + str(i) + '% ' + '*'*i, end='', flush=True)
#
#
# progress_bar()

# print('*'*100,  flush=True)
# print('*'*10, flush=True)


# import time
# for i in range(0,101,2):
#      time.sleep(0.1)
#      char_num = i//2
#      per_str = '\r%s%% : %s\n' % (i, '*' * char_num) \
#          if i == 100 else '\r%s%% : %s' % (i,'*'*char_num)
#      print(per_str,end='', flush=True)

# from math import sqrt
#
# def is_sqrt(x):
#     return str(sqrt(x))[-2:] == '.0'
#
#
# ret = filter(is_sqrt, list(range(100)[0:100]))
# for i in ret:
#     print(i)

# l = ['      ', [1, 2], 'hello world!']
# def len_x(x):
#     return len(x)
#
# print(sorted(l, key = len_x))


# t1 = (('a'), ('b'))
# t2 = (('c'), ('d'))
# r1 = list(map(lambda t: {t[0]: t[1]}, zip(t1, t2)))
# print(r1)
# r2 = lambda t1, t2: [{i: j} for i, j in zip(t1, t2)]
# print(r2(t1, t2))

# def multipliers():
#     return [lambda x:i*x for i in range(4)]
# print([m(2) for m in multipliers()])


# d = lambda p:p*2
# t = lambda p:p*3
# x = 2
# x = d(x)
# x = t(x)
# x = d(x)
# print(x)

# name = ['alex', 'wupeiqi', 'yuanhao', 'nezha']
# print(list(map(lambda x: x + '_sb', name)))
#
# num = [1, 3, 5, 6, 7, 8]
# print(list(filter(lambda x: x % 2 == 0, num)))

# s = ''
# n = 1
# with open('fenye.txt', mode='r+', encoding='utf-8') as f:
#     for i in f:
#         if len(i.strip()) > 0:
#             s = s + str(n) + '--' + i
#         n += 1
#     print(s)
#     f.seek(0)
#     f.write(s)


# with open('fenye.txt', mode='r', encoding='utf-8') as f:
#     l = f.readlines()
#
# rows_per_page = int(input('设置每页显示行数：').strip())
# while 1:
#     n = int(input('页码：').strip())
#     pages, mod = divmod(len(l), rows_per_page)  # 求可以分pages页，剩余mod行
#     if mod > 0:
#         pages += 1
#     if 0 < n <= pages:
#         print(''.join(list(filter(lambda x: l.index(x) in range(n*rows_per_page-rows_per_page, n*rows_per_page), l))))
#     else:
#         print('页码超出范围')

# #
# portfolio = [
#     {'name': 'IBM', 'shares': 100, 'price': 91.1},
#     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#     {'name': 'FB', 'shares': 200, 'price': 21.09},
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'ACME1', 'shares': 75, 'price': 115.65},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
#     {'name': 'ACME', 'shares': 75, 'price': 115.65}
# ]
#
# print('每支股票总额：', list(map(lambda x: {x['name']:x['shares'] * x['price']}, portfolio)))
# print('单价大于100的股票：', list(filter(lambda x: True if x['price'] > 100 else False, portfolio)))


# import sys, time
# sys.setrecursionlimit(100000)
# n = 1
#
#
# def story():
#     global n
#     print(n)
#     n += 1
#     time.sleep(0.01)
#     story()
#
#
# story()


# def find(l, aim, start = 0, end = None):
#     end = len(l) if end == None else end
#     mid_index = (start + end)//2
#     if l[0] <= aim <= l[-1]:
#         if start <= end:
#             if l[mid_index] < aim:
#                 return find(l, aim, start = mid_index + 1, end = end)
#             elif l[mid_index] > aim:
#                 return find(l, aim, start = start, end = mid_index - 1)
#             else:
#                 return mid_index
#         else:
#             return '找不到'
#     else:
#         return '找不到'
#
# l = [2,3,5,10,15,16,18,22,26,30,32,35,41,42,43,55,56,66,67,69,72,76,82,83,88]
# ret = find(l, 88)
# print(ret)
#
# 用递归函数实现斐波拉契数列，结果返回第n个数的值。
# import time
# def fibo(n, a=0, b=1):
#     if n >0:
#         c = a
#         a = b
#         b = b + c
#         n -= 1
#         return fibo(n, a, b)
#     else:
#         return a
#
# start1 = time.time()
# ret = fibo(600)
# end1 = time.time()
# print(ret)
# print('方法一', end1-start1)


# def fibo2(n, l = [0]):
#     l[0] += 1
#     if n == 1:
#         l[0] -= 1
#         return 0, 1
#     elif n == 2:
#         l[0] -= 1
#         return 1, 1
#     else:
#         a, b = fibo2(n-1)
#         l[0] -= 1
#         if l[0] == 0:
#             return b+a
#         return b, b+a
#
# start2 = time.time()
# ret = fibo2(5)
# end2 = time.time()
# print(ret)
# print('方法二', end2-start2)


# def jiecheng(n, ret = 1):
#     """
#     用递归函数求n的阶乘
#     :param n: 求n的阶乘
#     :param ret: 阶乘结果
#     :return: ret
#     """
#     if n > 0:
#         ret = ret*n
#         n -= 1
#         if n > 0:
#             if n > 1:
#                 print(str(n+1) + '*', end='', flush=True)
#             else:
#                 print(str(n+1) + '*1 ', flush=True)
#                 print('= ', end='')
#             return jiecheng(n, ret)
#         else:
#             return ret
#     else:
#         return '输入错误'


# result = jiecheng(5)
# print(result)

# 阶乘方法二：
# def jiecheng2(n):
#     if n == 1:
#         print('1=')
#         return n
#     else:
#         print(str(n) + '*', end='', flush=True)
#         return n*jiecheng2(n-1)
#
# ret = jiecheng2(5)
# print(ret)


menu1 = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}

# 方法一:老师的代码
# def duoji_menu(d, flag=0):
#     """
#     多级目录
#     :param d:
#     :param flag:
#     :return:
#     """
#     if flag == 0:
#         d = d
#         print('---', d)
#     for i in d:
#         print(i)
#     l1 = list(d.keys())
#     print(len(l1))
#     if len(l1):
#         # print('列表：', ' '.join(l1))
#         x = input('>>>').strip()
#         if x in l1 and x:
#             if d[x]:
#                 d = dict(d[x].items())
#                 flag += 1
#             return duoji_menu(d, flag)
#     else:
#         print(d)
#         return duoji_menu(d)
#
#
# ret = duoji_menu(menu1)
# print(ret)

# 方法二：递归   推荐
# def threeLM(dic):
#     while True:
#         for k in dic: print(k)
#         key = input('input>>>').strip()
#         if key == 'b' or key == 'q':
#             return key
#         elif key in dic.keys() and dic[key]:
#             ret = threeLM(dic[key])
#             if ret == 'q':return 'q'
#         elif (not dic.get(key)) or  (not dic[key]):
#             continue
# threeLM(menu1)

# 方法三：堆栈   推荐
# def threeLM(dic):
#     l = [dic]
#     while l:
#         for key in l[-1]: print(key)
#         k = input('input>>>').strip()
#         if k in l[-1].keys() and l[-1][k]:
#             l.append(l[-1][k])
#         if k == 'b':
#             l.pop()
#         if k == 'q':
#             break
# threeLM(menu1)


import re
# ret = re.findall('[^ ]+', 'abc sbad wsdfa')
# print(ret)

# ret = re.match('ab', 'abc sbad wsdfa')
# if ret:
#     print(ret.group())
#
# ret = re.sub('\d', 'H', 'sf2sdf4fwf5')
# print(ret)
#
# obj = re.compile('\d{3}')
# ret = obj.subn('H', 'sfds111ssdf32sdf333fd')
# print(ret)
#
# ret = re.finditer('\d', 's2sssf2df323d233d232')
# for i in ret:
#     if i:
#         print(i.group())


# ret = re.search("<(?P<tag_name>\w+)>\w+</(?P=tag_name)>", "<h1>hello</h1>")
# print(type(ret))
# if ret:
#     print(ret.group(0, 1))
#
# ret=re.findall(r"(-?\d+\.\d*)|-?\d+", "1-2*(60+(-40.35/5)-(-4*3))")
# print(ret)
#
# ret = re.findall('^[\u4e00-\u9fa5]{0,}$', '阿斯顿发生')
# print(ret)
#
# ret = re.findall(r'\s', '\s')
# print(ret)


# import queue
# q=queue.Queue()
# q.put(1)
# q.put(2)
# print(q.qsize())
# print(q.get())
# print(q.qsize())
# q.get()
# q.get()


# 阿里云消费订单表格式处理
# n = 0
# with open('txt/ali-zdxy.txt', mode='r', encoding='utf-8') as f1,open('txt/ali-zdxy-new.txt', mode='w', encoding='utf-8') as f2:
#     s = ''
#     for i in f1:
#         line1=re.findall('^\d{15}.*|^\d{6}.*', i)
#         if len(line1)>0:
#             n += 1
#             # print(line1)
#             s = s + '\n' + i + '\t'
#         else:
#             if '...详细' in i:
#                 i = i.replace('...详细', '')
#             if '￥' in i:
#                 i = i.replace('￥ ', '￥')
#             i = i.replace(' ', '-')
#             s = s.strip() + '\t' + i
#
#     # print('n=', n)
#     s = s.replace('\n\n', '\n')
#     f2.write(s)
#     print(s)

# from collections import defaultdict
# d=defaultdict(list)
# d['k']='a'
# print(d)
# print(d['l'])
# n=defaultdict(int)
# n['a']=5
# print(n)

# import time
# print(time.strftime('%Y-%m-%d %X'))
# print(time.strftime('%Y-%m-%d %H:%M:%S %j'))
# print(time.localtime())

# import os
# os.makedirs('1/2/3', exist_ok=True)
# os.removedirs('1/2/3')


# 序列化
import json
# dic = {'1': 'a', '2': 'b '}
# j = json.dumps(dic)
# print(type(j), j)
#
# dic1 = json.loads(j)
# print(dic1)

# d1 = {'1': 'a', '2': 'b '}
# with open('txt/xuliehua.txt', mode='w', encoding='utf-8') as f1:
#     json.dump(d1, f1)
#
# with open('txt/xuliehua.txt', mode='r', encoding='utf-8') as f2:
#     ret = json.load(f2)
# print(ret)
# import sys
# print(sys.path)

# from mokuai import read
# read()


# import json
# data = {'username':['李华','二愣子'],'sex':'male','age':16}
# json_dic2 = json.dumps(data,sort_keys=True,indent=2,separators=(',',':'),ensure_ascii=False)
# print(json_dic2)

# import os
# os.makedirs('glance/api')
# os.makedirs('glance/cmd')
# os.makedirs('glance/db')
# l = []
# l.append(open('glance/__init__.py','w'))       # 创建文件
# l.append(open('glance/api/__init__.py','w'))
# l.append(open('glance/api/policy.py','w'))
# l.append(open('glance/api/versions.py','w'))
# l.append(open('glance/cmd/__init__.py','w'))
# l.append(open('glance/cmd/manage.py','w'))
# l.append(open('glance/db/__init__.py','w'))
# l.append(open('glance/db/models.py','w'))
# print(l)
# map(lambda f:f.close() ,l)                     # 集中关闭打开的文件句柄


# import glance
# glance.cmd.manage.main()


# try:
#     sdf
# except Exception as e:
#     print('错了', e)


import 20191126

20191126.text()







