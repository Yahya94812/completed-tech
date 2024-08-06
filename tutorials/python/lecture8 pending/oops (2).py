#Static method
#work at class level and does't have self paremeter
class Static:
    
    @staticmethod
    def sum(x,y):
        print(x+y)

c1=Static()
Static.sum(3,45) 
c1.sum(3,45) 

# #del keyword
# #it is use to delet object property or object it self
# class Student:

#     def __init__(self,name):
#         self.name=name

# s=Student("yahya")
# print(s)
# print(s.name)
# del s.name #deleting object attribute
# print(s.name)
# del s #deleting the object
# print(s)

#private attribute and methods
#it is accesd in the class only and it is not accessable out side the class
class Account:
    def __init__(self,ac_no,ac_pass):
        self.ac_no=ac_no
        self.__ac_pass=ac_pass #{__} is used to make attribute or method private and it is accessed from class only
    def show(self):
        print(self.__ac_pass)    


p=Account("123","abc")
p.show()
print(p.__ac_pass)        
 


















