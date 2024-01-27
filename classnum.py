class num:
   def __init__(self,a):
    self.a=a
   def square(self):
    return self.a**2
   def cube(self):
    return self.a**3 
   def double(self):
    return self.a*2
   def iseven(self):
    if self.a%2==0:
        return True
    else:
        return False
   def isprime(self):
    flag=True
    if self.a>1:
        for val in range(2,self.a):
            if self.a% val ==0:
                flag = False
                break
            return flag 
    def factorial (self):
        out = 1
        if self.a>1:
           for val in range(1,self.a+1):
              out*=val
           return out  
