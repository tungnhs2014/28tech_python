
class Person:
    def __init__(self):
        print('Ham khoi tao cua lop cha')
    def xinchao(self):
        print('Person xin chao\n')

class Student (Person):
    def __init__(self):
        print('Ham khoi tao cua lop con')

if __name__ == '__main__':
    s = Student()
    s.xinchao()
        