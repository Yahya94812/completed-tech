#first creat a class then creat objects of that class
#lists, strings etc are the objects
#class is the blue print of the object
#start class name with capital letters {optional}
#object is also called instances
#first paremeter of constructer that is {__init__ function} is always self {self word is optional}
#self is refer to every newly created object
#two type of cunstructor 1.parametarize {that contain more than one paremeter including self} 2.default cunstructor
#if ther is more than one cunstructor than the constructor that matchs the no of paremeter get exicuted
#a class may contain attribute{property} and a function called methods

class stu:
    name="yahya" #class atribute
    def __init__(self): #constructor is executed at the time of creation of every object if it is not define a default constructor {that does't take any paremeter other than self} get executed and it is refer to the object
        print("i am in constructer")

s1=stu() #the paranthisis followed by class name is for the creation of the object is use for calling the instructor function
print(stu.name) #1.accissing class atribute
print(s1.name) #2.accissing class atribute

print()

class student:
    def __init__(self,name):
        print("adding new name ..")
        self.naam=name # instance atribute {usually replace "naam" by "name" only as a good programmer}

st1=student("yahya")
print(st1.naam) #accessing object atribute    

print()

class office:
    name="class"
    def __init__(self,name): #object atributes has higher priority than class atribute
        self.name=name

employ=office("object")
print(employ.name)        
             
print()

#methods
class methods:
    def __init__(self,name):
        self.name=name
    def name(self):
        print(self.name)
    
s1=methods("yahoo")
s1.name()    

#Static method
class Static:
    @staticmethod
    def sum(x,y):
        print(x+y)
    c1=Static()
    Static.sum(3,45)  