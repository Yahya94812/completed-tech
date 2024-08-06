class Stu:
    def __init__(self,name,roll):#constuctor is used for setuping initialized object
        self.name=name
        self.roll=roll

    def sum(self,a,b):
        self.sum=a+b
                

s=Stu("yahya",14)
print(s.name,s.roll,s.sum(3,4))        