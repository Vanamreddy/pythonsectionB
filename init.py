class Mtca:
  principal='prabhakar sir'
  college='Mtca'
  location='melumoi'
  def __init__(self,name,email,mob,sem):
    self.name = name
    self.email= email
    self.phone= mob
    self.sem  =sem
  def update_mob(self,new):
    self.mobile =new
    print('mobile number updated')
  @classmethod
  def change_principal(cls,new):
    cls.principal=new
  @staticmethod
  def add(a,b):
    return a+b     
mohan   =  Mtca ('mohan',6325867438,'mohan@gmail.com','1st')
mounika = Mtca('mounika',6921470174,'mounika@123','2nd')    

  
 

