class Add:
    @staticmethod
    def add2(a,b):
        return a+b
    @staticmethod
    def add3(a,b,c):
        return a+b+c
class Sub:
    @staticmethod
    def sub2(a,b):
        return a-b
class Mul:
    @staticmethod
    def mul2(a,b):
        return a*b
class cal(Add,Sub,Mul):
    pass
obj= cal()
print(obj.add2(3,4))#7
print(obj.add3(4,5,6))#15
print(obj.mul2(2,4))#8
print(obj.sub2(5,2))#3           