class  grandparents:
    a=10
    b=20

    def __init__(self,c,d):
        self.c = c
        self.d = d
    def display(self):
        print(self.c,self.d)

class parent(grandparents):
    a=30
    
    def __init__(self,c,d,e,f,):
        super().__init__(c,d)
        self.e = e
        self.f = f
    def display(self):
        #parent.display(self)
        super().display()
        print(self.e,self.f)
    def child(parents):
     
     a=50

    def __init__(self,c,d,e,f,g,h):
        super().__init__(c,d,e,f)
        self.g = g
        self.h = h
        print(self.g,self.h)
        
    obj=child(4,5,6,7,8,9)    