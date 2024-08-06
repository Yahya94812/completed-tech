#both class method and static method are associated with class rather then objects but there is some diffrence between them
#class methods are use to accessing and changing class level attributes or variables and creating new objects of the class 
#static methods are related to class somewhere but does't requare to access class level attributes or variables and it is same like a regular function and it is write in class for organization purposes

class Stu:

    x=10

    @staticmethod
    def hello():
        return "hello world"
    @classmethod
    def ClassV(cls):
        return cls.x
    
print(Stu.hello()) 
print(Stu.ClassV())   