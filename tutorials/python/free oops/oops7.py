class Stu:
    def __init__(self,name,roll_no):
        self.__name=name
        self.__roll_no=roll_no

    def show_name(self):
        return self.__name#attribute leading with {__} can accessed only by class methods

    @property
    def read_only(self):
        return self.__roll_no

s1=Stu("yahya",76)
print(s1.show_name())
s1.name="no name"#once the name is renamed it is not effected by {__}
print(s1.name)        

print(s1.__roll_no)