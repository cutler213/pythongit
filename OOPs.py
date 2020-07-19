
class student:
    schoool='teulusko'

    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def avg(self):
        return (self.m1+self.m2)/2

    @classmethod
    def info(cls):
        return cls.schoool

    @staticmethod
    def sqr(x):
        return x*x


s1=student(21,22)

print(student.sqr(2))