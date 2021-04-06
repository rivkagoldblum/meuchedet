class Basic:
    def __init__ (self):
#           self.name = name
#       self.tz = tz
        self._cost = 100
    def therapy(self):
        return('The client is not entitled to any therapy.')
    def set_cost(self, value):
        self.cost = value
        return()    
    def get_cost(self):
        return self._cost  
class Adif(Basic):
    def __init__ (self):
        super().__init__()
        self._cost+=50
    def therapy(self):
        return('The client is entitled to swimming therapy.')
class C(Adif):
    def __init__ (self):
        super().__init__()
        self._cost += 50        
    def therapy(self):
        return('The client is entitled to swimming and horseriding therpay.')
patient1 = Basic()
patient2 = Adif() 
patient3 = C() 
#print(patient1.therapy())   
#print(patient2.therapy()) 
#print(patient3.therapy()) 
#print(patient1.get_cost())
#print(patient2.get_cost())
#print(patient3.get_cost())



