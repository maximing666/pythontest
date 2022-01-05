print('hello world.','你好')
#name=input()
#print('你的名字是：',name)
print(r'\\//t\n')
print('''sdfsd
pass
sdfsd''')

sum=0
for x in range(101):
    sum=sum+x
print(sum)

#dict
d={'tom':89,'linda':98}
print(d)
print(d['tom'])
print(d.get('jack',-1))
print('jack' in d)
d.pop('tom')
print(d)

#函数
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('x is the bad operant type.')
    if x>=0:
        return x
    else:
        return -x
print("my_abs(-2)=",my_abs(-2))


def f2(a, b, c=0, *, d, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'd=', d, 'kw=', kw)
args=(1,2,3)
kw={'d':88,'x':'#'}
#  *可变参数 **关键字参数
print(f2(*args,**kw))

#斐波拉契函数
def fib(max):
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n=n+1
    return 'done'

fib(10)

print('---------------------')
#斐波拉契生成器
def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    return 'done'

f=fib(6)
print('f的数据类型:',type(f))
for i in f:
    print(i)

print('------------')
def odd():
    print('1')
    yield 1
    print('2')
    yield
    print('3')
    yield (3)

o=odd()
for i in o:
    print(i)

print('------------')

print('--vvvvv------map,reduce')
def normalize(name):

    return name.capitalize()

L1 = ['adam', 'LISA', 'barT']

L2 = list(map(normalize, L1))

print(L2)


def normalize(name):
    name=name.lower()
    return name[0].upper()+name[1:]

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

from functools import reduce
def prod(L):
    def ji(x,y):
        return x*y
    return reduce(ji,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

print('-----质数方法一----filter')
def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n

def _not_divisible(n):
    return lambda x:x%n>0
def primes():
    yield 2
    it=_odd_iter()
    while True:
        n=next(it)
        yield n
        it=filter(_not_divisible(n),it)
#print <100的素数（及质数）
for n in primes():
    if n<100:
        print(n)
    else:
        break

print('--质数：方法二-----')
from math import sqrt
def a(n):
    if n>3:
        for i in  range(2,int(sqrt(n))+1):
            if n % i == 0:
                break
            else:
                return n
    elif n==2:
        return n
    elif n==3:
        return n

l=[2,3,4,5,6,7,11,13,15,17]
r=filter(a,l)
print(type(r))
print(list(r))

print('------vvvvv-----计算回数')
def is_palindrome(n):
    s=str(n)
    l=len(s)
    i=0
    while i<l//2:
         if s[i] == s[l-i-1]:
            i=i+1
         else:
            break
    if i==l//2:
        return n



# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('回数测试成功!')
else:
    print('回数测试失败!')


print('-----vvvvvvvvv---sorted')

L = [('Bob', 75), ('Adam', 92),('Core',86), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
L2 = sorted(L, key=by_name)
print(L2)

print('----------')
L = [('Bob', 75), ('Adam', 92),('Core',86), ('Bart', 66), ('Lisa', 88)]
def by_score(t):
    return -t[1]

L3 = sorted(L, key=by_score)
print(list(L3))

print('-----vvvvvvv----返回函数')
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1,f2,f3=count()
print(f1(),f2(),f3())


print('----------------OOP')
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
bart=Student('Bart Simpson',59)
bart.age1=8
print('bart age1:',bart.age1)


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self,gender):
        if gender == 'male' or gender == 'female':
            self.__gender=gender
        else:
            raise ValueError('bad gender')



bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')

print('----------继承、多态')
class Animal(object):
    def run(self):
        print('Animal is running...')



class Dog(Animal):
    def run(self):
        return 'Dog is running...'


class Cat(Animal):
    def run(self):
        return 'Cat is running...'


a=Animal()
d=Dog()
c=Cat()
print(a.run(),'\t\n',d.run(),'\t\n',c.run())

def run_twise(animal):
    animal.run()
    animal.run()
print('run_twise:',run_twise(Animal()))

print('--------获取对象信息')
class MyObject(object):
    def __init__(self):
        self.x=9
    def power(self):
        return self.x * self.x
mo=MyObject()
print(hasattr(mo,'x'))
print(mo.x)
print(hasattr(mo,'y'))
setattr(mo,'y',100)
print(hasattr(mo,'y'))
print(mo.y)
print(getattr(mo,'y'))
print(getattr(mo,'w',404))

print('------实例属性，类属性')
class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1


if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')

print('-------property')
class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an int.')
        if value<0 or value >100:
            raise ValueError('score must between 0 ~ 100')
        self._score=value
s=Student()
s.score=60
print('s.score=',s.score)
#s.score=160
print(s.score)

print('------iter')
class Fib(object):
    def __init__(self):
        self.a,self.b=0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a
for n in Fib():
    print(n)

print('-----链式调用')
class Chain(object):
    def __init__(self,path=''):
        self._path=path

    def __getattr__(self, path):
        return Chain('%s/%s'%(self._path,path))

    def __str__(self):
        return self._path

    __repr__=__str__

print(Chain().status.user.time.line.list)

print('----------枚举')
from enum import Enum
Month=Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
for name,member in Month.__members__.items():
    print(name,'=>',member,',',member.value)

print('')
from enum import Enum,unique
@unique
class Weekday(Enum):
    Sun=0
    Mon=1
    Tue=2
    Wed=3
    Thu=4
    Fri=5
    Sat=6

print(Weekday.Sun)
print(Weekday.Sun.value)
print(Weekday.Sun.name)
print(Weekday(0))

'''
print('------单元测试')
import unittest
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score >= 60 and self.score <80:
            return 'B'
        if self.score >= 80 and self.score <=100:
            return 'A'
        if self.score >=0 and self.score <60:
            return 'C'
        else:
            raise ValueError


class TestStudent(unittest.TestCase):

    def test_80_to_100(self):
        s1 = Student('Bart', 80)
        s2 = Student('Lisa', 100)
        self.assertEqual(s1.get_grade(), 'A')
        self.assertEqual(s2.get_grade(), 'A')

    def test_60_to_80(self):
        s1 = Student('Bart', 60)
        s2 = Student('Lisa', 79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_to_60(self):
        s1 = Student('Bart', 0)
        s2 = Student('Lisa', 59)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    def test_invalid(self):
        s1 = Student('Bart', -1)
        s2 = Student('Lisa', 101)
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()

if __name__ == '__main__':
    unittest.main()

'''
'''
print('-----------读写文件')
with open('d:\\123.txt','r') as f:
    print(f.read())
'''
print('-----------StringIO')
from io import StringIO
f=StringIO('Hello one.\n Hello two.\nHello Three.')
while True:
    l=f.readline()
    if l=='':
        break
    print(l.strip())

print('-----------BytesIO')
from io import BytesIO
f=BytesIO('中国'.encode('utf8'))
print(f.getvalue())
print(f.read())


print('--------序列化 json')
import json
obj = dict(name='小明', age=20,sex='男')
s = json.dumps(obj, ensure_ascii=True)
print(s)



print('---------------正则表达式')
import re
def is_valid_email(addr):
    re_e=re.compile(r'(\w+[.]?\w+)@(\w+).([a-z|A-Z]+)')
    if re_e.match(addr):
        return True
    else:
        return False

assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')

