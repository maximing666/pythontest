import sys
class Teacher:
    menu = {
        '查看课程': 'show_course',
        '管理班级': 'manage_class',
        '查看学员': 'show_student',
        '修改成绩': 'alter_score',
        '退出': 'quit'
    }

    def __init__(self, name):
        self.name = name
        # self.classes = classes
        # self.course = classes

    def show_cource(self):
        pass

    def manage_class(self):
        pass

    def show_student(self):
        pass

    def quit(self):
        sys.exit()


