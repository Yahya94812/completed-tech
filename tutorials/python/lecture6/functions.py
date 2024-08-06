#user define function
def calsum(a,b): #a and b are paremeter
    sum=a+b
    print(sum)
    return sum #if not written function return Nune and control

s=calsum(3,4) #hear a and b are argument
print(s)

def calsum(a,b=1): #b is a default value if not pass argument from calling function and it is always start from last to first
    sum=a+b
    print(sum)
    return sum #if not written function return Nune

s=calsum(3) #hear a and b are argument
print(s)


#built in function
print("md","yahya") #blank space between words in output due to comma {in built function}

print("mohd",end=" ")#print in the same line because default is end="\n"
print("yahya")#print in the same line because default is end="\n"
print() #it is use for \n

#len(),range(),type() are also built in function


#recursion

def fact(a):
    if a==1: #this is called basecase in recursion
        return 1
    else:
        return a*fact(a-1)
x=fact(5)        
print(x)        