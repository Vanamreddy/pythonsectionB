from abc import ABC,abstractmethod
class  modelcar(ABC):
    @abstractmethod
    def Break():
      pass
    @abstractmethod
    def speed_up():
       pass
    @abstractmethod
    def speed_down():
       pass
class brezza(modelcar):
    def __init__(self,speed=0,stop=True):
       self.speed = speed
       self.stop =stop
    def speed_up(self):
       self.speed+=45
       self.stop = False
    def Break(self):
       self.speed = 0
       self.stop = True
    def speed_down(self):
       if not self.stop:
          self.speed -=5
          if self.speed == 0:
            self.speed = True      
       

    