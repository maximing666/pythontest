# 实现能计算类似
# 1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )等类似公式的计算器程序.
import re

# def normal_yunsuan(x, flag=None):
#     if flag == None:
#         x = x
#     if x.find(r'*') > 0 or x.find(r'/') > 0:
#         # l1 = re.search(r'\d+\.?\d*[\*\/]\d+\.?\d*', x)
#         l1 = re.search(r'\d+\.?\d*[\*\/]\(?\-?\d+\.?\d*\)?', x)
#         if l1:
#             i = l1.group()
#             index1 = i.find('*')
#             index2 = i.find('/')
#             if index1 > 0:
#                 x = x.replace(i, str(float(i[0:index1])*float(i[index1+1:])))
#             if index2 > 0:
#                 x = x.replace(i, str(float(i[0:index2]) / float(i[index2 + 1:])))
#         flag = 1
#         return normal_yunsuan(x, flag)
#     elif x.find(r'+') > 0 or x.find(r'-') > 0:
#         l1 = re.search(r'\d+\.?\d*[\+\-]\d+\.?\d*', x)
#         if l1:
#             i = l1.group()
#             index1 = i.find('+')
#             index2 = i.find('-')
#             if index1 > 0:
#                 x = x.replace(i, str(float(i[0:index1]) + float(i[index1 + 1:])))
#             if index2 > 0:
#                 x = x.replace(i, str(float(i[0:index2]) - float(i[index2 + 1:])))
#         flag = 1
#         return normal_yunsuan(x, flag)
#     else:
#         print('x=', x)
#         return x

# ret = normal_yunsuan('9-2*5/3+7/3*99/4*2998+10*568/14')
# print('ret:', ret)

# def yunsuan(inp=0, flag = None):
#     if flag == None:
#         # inp = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
#         inp = inp
#         inp = inp.replace(' ', '')
#     l1 = re.findall(r'(\([\+\-\*\/\d+\.?\d*]+\))', inp)
#     print(l1)
#     for i in l1:
#         i1 = i.replace('(', '')
#         i2 = i1.replace(')', '')
#         print(i2)
#         ret1 = normal_yunsuan(i2)
#         inp = inp.replace(i2, ret1)
#     l2 = re.findall(r'[\+\-\(]\(\-\d+\.?\d*\)', inp)
#     print('l2:', l2)
#     print(inp)
#     for j in l2:                    # 去掉（-12.12）
#         if re.match('\+', j):
#             inp = inp.replace(j, re.findall('\-\d+\.?\d*', j)[0])
#         elif re.match('\-', j):
#             inp = inp.replace(j, '+' + re.findall('\d+\.?\d*', j)[0])
#         elif re.match('\(', j):
#             inp = inp.replace(j, re.findall('\(\-\d+\.?\d*', j)[0])
#     print(inp)
#     l3 = re.findall(r'\(\d+\.?\d*\)', inp)
#     for m in l3:     # 去掉 （12.12）
#         inp = inp.replace(m, re.findall('\d+\.?\d*', m)[0])
#     print(inp)
#     l4 = re.findall(r'[\+\-]?\d+\.?\d*[\*\/]\(\-\d+\.?\d*\)', inp)
#     print('l4:', l4)
#     for n in l4:
#         if re.match('\+?\d', n):
#             x = '-' + re.findall(r'\d+\.?\d*', n)[0] + re.findall('[\*\/]', n)[0] + re.findall(r'\d+\.?\d*', n)[1]
#             ret2 = normal_yunsuan(x)
#             inp = inp.replace(n, ret2)
#         elif re.match('\-\d', n):
#             x = '+' + re.findall(r'\d+\.?\d*', n)[0] + re.findall('[\*\/]', n)[0] + re.findall(r'\d+\.?\d*', n)[1]
#             ret2 = normal_yunsuan(x)
#             inp = inp.replace(n, ret2)
#     if inp.find('*') < 0 and inp.find('/') < 0:
#         ret3 = normal_yunsuan(inp)
#         return ret3
#     flag = 1
#     return yunsuan(inp, flag)
#
# r=yunsuan('1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3)))')
# print('运算结果：', r)
# print(eval('1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 )))'))



#     import random
# def yanzhengma(n):
#     """
#     输出验证码，验证码由大小写字母及数字组成
#     :param n: 验证码的位数
#     :return: 验证码
#     """
#     l1=[]
#     l1 = l1 + list(range(65, 91))
#     l1 = l1 + list(range(97, 123))
#     l1 = l1 + 2*list(range(0, 10))  # 添加两次主要是因为数字共10个，比字母的出现概率低
#     random.shuffle(l1)  # 打乱原始库
#     print(l1)
#     s = ''
#     while n > 0:
#         sa = random.choice(l1)   # 随机抽取一个数字
#         if sa > 9:
#             s = s + ' ' + chr(sa)
#         else:
#             s = s + ' ' + str(sa)
#         n -= 1
#     return '验证码：' + s
#
# ret=yanzhengma(10)
# print(ret)