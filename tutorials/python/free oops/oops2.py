class Items:
    all=[]#class attribute
    def __init__(self,name,qt,mrp):
        self.name=name
        self.qt=qt
        self.mrp=mrp
        Items.all.append(self)

    def __repr__(self):#repr stand for representing your objects
        return f"Items('{self.name}',{self.qt},{self.mrp})"   #formatted string 

    @classmethod #class methods modify class attributes etc at class level
    def hello(cls):
        print(f"all the object from class attributes are {cls.all}")


item1=Items("cpu",1,1000)

item2=Items("keys",3,100)
print(Items.all)

for i in Items.all:
    print(i.name)

for i in Items.all:
    print(i.qt)

Items.hello()