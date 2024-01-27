class mtca:
    chairman = 'mr.sunil'
    location = 'palamaner'
    college  = 'mtca'
    
    def __init__(self,name,mobile):
        self.name = name
        self.mobile = mobile

class mca(mtca):
    principal = 'mr.prabhakar naidu'
    strength   = 240
    staff     = 9
class btech(mtca):
    principal = 'ms.mounika'
    strength  = 350
    staff     = 35
indhu = mca('indhu',6374915825)
janu  = btech('janu',7345975879)              