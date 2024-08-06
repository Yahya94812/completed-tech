#super method give more precise control for calling parent class methods
#if init function is defined in child class then init of parent class is ignored


class Students:

    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no

    def cls_name(self):
        return self.__class__.__name__#it print the name of class to which it belongs

class Toppers(Students):
    def __init__(self,name,roll_no,gold_medal=0):
        self.gold_medal=gold_medal
        super().__init__(name,roll_no)
        

s1=Toppers("yahya",14)
s2=Students("yahya",14)
print(s1.cls_name())
print(s2.cls_name())
