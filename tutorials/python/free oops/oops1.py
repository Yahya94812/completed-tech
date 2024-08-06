#variables are the reference of objects and objects actully store the values and these objects belongs to different class like int, float, list etc

class Item:
    pass
aitem=Item()
aitem.name="yahya"
print(type(aitem))#<class '__main__.Item'>#if the class is in diffrent file then [__main__] is replaced by the file name in wich class is defined with out [.py]
print(type(aitem.name))#<class 'str'>

print()

class Books:
    def tprice(self,rs,qt):#function in class is called methods
        return rs*qt
b1=Books()
b1.qt=2
b1.rs=10
tp=b1.tprice(b1.rs,b1.qt)
print(tp)

print()

class Products:
    def __init__(self,rs:float,qt=1):#qt=1 is the default value if it is not pass as argument and rs:float convert rs to float data type if possible
        self.rs=rs
        self.qt=qt
    def tprice(self):
        return self.rs*self.qt
b1=Products("10",2)
print(b1.rs,b1.qt)
print(b1.tprice())
b2=Products(12,5)
b2.name="p"
print(b2.__dict__)#print all attrebutes of instance level
print(Products.__dict__)#print all attributes of class level