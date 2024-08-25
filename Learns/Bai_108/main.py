
class Person:
    nationality = "VietNam"
    def __init__(self, name, job):
        self.name = name
        self.__job = job #private
    def Get_name(self):
        return self.name
    def Get_job(self):
        return self.__job
    def Set_name(self, name):
        self.name = name
    def Set_job(self, job):
        self.__job = job

if __name__ == '__main__':
    p1 = Person('Tung', 'Dev')
    print(p1.Get_name())
    print(p1.Get_job())
    p1.Set_job("Embedded")
    print(p1.Get_job())
