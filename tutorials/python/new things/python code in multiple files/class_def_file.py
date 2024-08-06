class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll

print(__name__)
if __name__=="__main__":#the __name__ variable store __main__ if the script is run directly else the __name__ in built variable is replaced by the name of the file in wich the class is located i.e.. "class_def_file" in this case
    s1=Student("yahoo in __main__",14)
    print(s1.name,"\n",s1.roll)
    

