#python is case sensitive language and it is implicit data type language
# click both check boxes while installing python setup
# identifer is any name like variable name or function name etc
# identifers does't start with numbers and don't use spacial symbols and keywords in identifers but it may be start with {_}
#use {""" abc """} for multiple line and {#} for single line comment 


print("hello")#in diffrent lines
print("world")#in diffrent lines
print("hello","world")#in the same line

print("mohammed \nyahya")
print("mohammed \tyahya")#use \t for tab space

print(29)#printing int
print(9-5)#arthematic opreation

name,age="yahya",19
print("my name is :",name)
print("my age is :",age)

print(type(name))
print(type(age))

 
#strings can be written in single , double , triple {',",'''} etc quotes 
a,b=2,4
str1,str2="@","$"
print(3*str1)
print((str1+str2)*3)


#simple division and integer division({//} and it is with out round off) always produse float values
print(-5//2)#it produce -3 not -2{ie.. least value}
print(5%(2))
print(5%(-2))#when denominator is negative answer is negative
print(-5%(2))#when nomenator is negative answer is positive

#use {**} for finding powers of numbers


name=input("enter your name :")#default input type is string
age=int(input("enter your age :"))
print("your name is",name,"\nyour age is",age)


#type casting
a=10
print(type(a))
b=str(a)
print(type(b))

b="14"
a=int(b)
print(type(a))


#in boolean data type True and False {first letter must be capital}
old=False#you can also declare boolean as a simple variable
young=True#you can also declare boolean as a simple variable
#precedence in logical operator {not>and>or}


if(True):#it definitly exicute the if block
    print("definitly")

num=int(input("enter the num :"))
if(num==1 or num==2):
    print("one or two")
elif(num==3):
    print("three")
else:
    print("out of range")   

num=int(input("enter a value:"))
str="false" if num==0 else "true"
print(str)

num=int(input("enter :"))
print("false") if num==0 else print("true") 