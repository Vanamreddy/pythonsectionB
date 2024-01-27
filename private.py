class cname:
    __a=10
    b=20
    def __init__(self,c,d):
        self.__c = c
        self.d = d
    def __display(self):
        print(self.c,self.d)
    @classmethod    
    def classdisplay(cls):
        print(cls.__a,cls.b)    
obj = cname(5,6)