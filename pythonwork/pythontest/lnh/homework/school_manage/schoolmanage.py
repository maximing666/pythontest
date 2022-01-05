# 面向对象作业——校园管理系统
# 角色:
# 学校、学员、课程、讲师
#
# 要求:
# 1. 创建北京、上海 2 所学校
#
# 2. 创建linux , python , go 3个课程 ， linux\py 在北京开， go 在上海开
#
# 3. 课程包含，周期，价格
#
# 4. 班级关联课程、讲师
#
# 5. 创建学员时，选择学校，关联班级
#
# 5. 创建讲师角色时要关联学校
#
# 6. 提供三个角色视图
#
# 　　6.1 学员视图， 登陆， 查看课程、查看班级
#
# 　　6.2 讲师视图， 讲师可查看自己教学的班级、课程。
#
# 　　　　　　　　　 进阶需求：可管理自己的班级， 查看班级学员列表 ， 修改所管理的学员的成绩
#
# 　　6.3 管理视图，创建讲师， 创建班级，创建课程
#
# 7. 上面的操作产生的数据都通过pickle序列化保存到文件里

# 分析：有几个类：学校、学员、课程、讲师、管理员、班级、成绩


from abc import abstractmethod, ABCMeta


class Person(metaclass=ABCMeta):     # 接口类（讲师、学员、管理员）
    def __init__(self, name, passwd):
        self.name = name
        self.__passwd = passwd

class School():
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr

@abstractmethod
class Student():
    def __init__(self, name, passwd):
        self.name = name
        self.__passwd = passwd
        self.school = School().name
        self.grade = Grade().name

@abstractmethod
class Teacher():
    def __init__(self, name, passwd):
        self.name = name
        self.__passwd = passwd
        self.school = School().name

@abstractmethod
class Manager():
    def __init__(self, name, passwd):
        self.name = name
        self.__passwd = passwd

    def create_course(self, *args):
        return Course(args)

    def create_teacher(self, *args):
        return Teacher(args)

    def create_student(self, *args):
        return Student(args)

    def create_grade(self, *args):
        return Grade(args)

class Course():
    def __init__(self, name, period, price):
        self.name = name
        self.period = period
        self.price = price
        self.addr = School().addr

class Grade():
    def __init__(self, name):
        self.name = name
        self.teacher = Teacher().name
        self.course = Course().name

class Score():
    def __init__(self, score):
        self.name = Student.name
        self.grade = Grade.name
        self.course = Course.name
        self.score = score


sch_bj = School('培训大学', '北京')
sch_sh = School('培训大学', '上海')

