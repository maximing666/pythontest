# class Person():
#     def __init__(self, *args):
#         self.name = args[0]
#         self.age = args[1]
#         self.sex = args[2]
#
#     def walk(self):
#         print('%s要走走走' % self.name)
#
#     def kanchai(self):
#         print('%s,%d岁,%s,上山去砍柴'%(self.name, self.age, self.sex))
#
#     def dongbei(self):
#         print('%s,%d岁,%s,开车去东北' % (self.name, self.age, self.sex))
#
#     def baojian(self):
#         print('%s,%d岁,%s,最爱大保健' % (self.name, self.age, self.sex))
#
# xiaoming = Person('小明', 10, '男')
# xiaoming.kanchai()
# xiaoming.dongbei()
# xiaoming.baojian()


# 求圆面积、周长
# from math import pi
# class Circle():
#     def __init__(self, r):
#         self.r = r
#
#     def zhouchang(self):  # 圆周长
#         return 2*pi*self.r
#
#     def mianji(self):  # 圆面积
#         return pi*self.r*self.r
#
# y1 = Circle(10)
# l = y1.zhouchang()
# s = y1.mianji()
# print(l,s)


# 求正方形的周长、面积
# class Zhengfangxing():
#     def __init__(self, l):
#         self.l = l
#
#     def zhouchang(self):
#         return self.l*4
#
#     def area(self):
#         return self.l**2
#
#
# zfx = Zhengfangxing(5)
# print(zfx.zhouchang())
# print(zfx.area())


# 游戏人狗大战
# class Person():
#     def __init__(self, *args):
#         self.name = args[0]
#         self.blood = args[1]
#         self.aggr = args[2]
#
#     def attac(self, dog):
#         dog.blood -= self.aggr
#         if dog.blood >0 :
#             print('%s被%s打了, 掉血%s, 剩血%s'%(dog.name, self.name, self.aggr, dog.blood))
#         else:
#             print('%s被%s打死了' % (dog.name, self.name))
#
# class Dog():
#     def __init__(self, *args):
#         self.name = args[0]
#         self.blood = args[1]
#         self.aggr = args[2]
#
#     def bite(self, person):
#         person.blood -= self.aggr
#         if person.blood >0 :
#             print('%s被%s咬了, 掉血%s, 剩血%s'%(person.name, self.name, self.aggr, person.blood))
#         else:
#             print('%s被%s咬死了' % (person.name, self.name))
#
#
# zhangsan = Person('张三', 100, 5)
# lisi = Person('李四', 100, 3)
# teddy = Dog('泰迪', 100, 20)
#
# teddy.bite(lisi)
# lisi.attac(teddy)
# teddy.bite(lisi)
# teddy.bite(lisi)
# lisi.attac(teddy)
# teddy.bite(lisi)
# teddy.bite(lisi)
# teddy.bite(lisi)


# from math import pi
# class Circle:
#     def __init__(self, r):
#         self.r = r
#
#     @property
#     def perimiter(self):
#         return 2*pi*self.r
#     @property
#     def area(self):
#         return pi*self.r**2
#
#
# c = Circle(5)
# print(c.area)
# print(c.perimiter)
# print(Circle.__bases__)

# from abc import abstractmethod, ABCMeta
# class Payment(metaclass=ABCMeta):
#     @abstractmethod
#     def pay(self, money):
#         pass
#         # raise NotImplementedError       # 加了ABCMeta, abstractmethod装饰器后，raise句可不用了
#
#
# class Wechatpay(Payment):
#     def zhifu(self, money):
#         print('微信支付了%s元'%money)
#
#
# class Alipay(Payment):
#     def pay(self, money):
#         print('微信支付了%s元'%money)
#
#
# def pay(pay_obj, money):
#     '''
#     支付函数，总体负责支付
#     对应支付的对象和要支付的金额
#     '''
#     pay_obj.pay(money)
#
#
# wechat = Wechatpay()
# ali = Alipay()
# pay(wechat, 200)
# pay(ali, 100)



# 封装  私有属性、私有方法、静态私有属性
# class Person():
#     __key = 123
#     def __init__(self, name, passwd):
#         self.name = name
#         self.__passwd = passwd
#         self.__mypasswd = self.__key*self.__passwd
#
#     def __get_mypasswd(self):
#         return self.__mypasswd
#
#     def __get_passwd(self):
#         return self.__passwd
#
#     def login(self):
#         return self.__get_passwd()
#
#     def login_key(self):
#         return self.__get_mypasswd()
#
# person = Person('alex', 3721)
# print(person.login())
# print(person.login_key())


# property
# class Goods():
#     __discount = 1
#     def __init__(self, name, price):
#         self.name = name
#         self.__price = price
#
#     @classmethod
#     def discount(cls, newdiscount):
#         cls.__discount = newdiscount
#
#     @property
#     def price(self):
#         return self.__price * self.__discount
#
#     @price.setter
#     def price(self, newprice):
#         self.__price = newprice
#
#     @price.deleter
#     def price(self):
#         del self.__price
#
#
# g = Goods('二锅头', 100)
# print(g.price)
# # g.discount(7.5)
# # print(g.price)
# g.price = 0.7
# print(g.price)
# del g.price
# # print(g.price)
#
# g1 = Goods('剑南春', 1000)
# print(g1.price)
#
# Goods.discount(0.3)  # 修改折扣值
# print(g1.price)


# class Login():
#     def __init__(self, name, passwd):
#         self.name = name
#         self.__passwd = passwd
#
#     @staticmethod
#     def get_user_pwd():
#         user = input('user name>>>').strip()
#         passwd = input('password>>>').strip()
#         return Login(user, passwd)
#
#
# ret = Login.get_user_pwd()
# print(ret.name, ret._Login__passwd)


#  反射
class Teacher():
    menu = {'查看学生信息': 'show_student', '查看讲师信息': 'show_teacher'}
    def __init__(self, name, pwd):
        self.name = name
        self.__pwd = pwd

    @staticmethod
    def func():
        print('hahhahah')

    @staticmethod
    def show_student():
        print('show_student方法内容')

    @classmethod
    def show_teacher(cls):
        print('show_teacher方法内容')

# ret = getattr(Teacher, 'menu')
# print(ret)
# if hasattr(Teacher, 'func'):
#     ret1 = getattr(Teacher, 'func')
#     ret1()
#
# print(getattr(Teacher, 'menu'))
# for i in Teacher.menu:
#     print(i)
# input1 = input('输入>>>').strip()
# b = hasattr(Teacher, Teacher.menu[input1])
# if b:
#     ret = getattr(Teacher, Teacher.menu[input1])
#     ret()

# teacher = Teacher('alex', '123')
# print(getattr(teacher, 'name'))
# getattr(teacher, 'show_student')()

import sys
def text():
    print('TEXT')
    print(sys.modules['__main__'])

getattr(sys.modules['__main__'], 'text')()















