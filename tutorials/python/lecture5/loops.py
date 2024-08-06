#the while loop
i=0
while True: #exicute infinite times
    i+=1 #i=i+1
    if i==5:
        continue #control go back to the head
    print(i)
    if i==10:
        break #loop is terminated

i=0
while True: #exicute infinite times
    i+=1 #i=i+1
    if i==5:
        pass #it means do nothing ie.. place holder and can be use with loops and conditional statements
    print(i)
    if i==10:
        break #loop is terminated


#the for loop
li=[1,2,3,4,5]
for l in li: #use in lists, strings to access elements
    print(l)  


#the range() function
ran=range(0,20,2) #it return the elements in range data structure like list, tuples, etc
print(type(ran))
listr=list(ran)  #type casting
print(type(listr))
print(listr)  

for i in range(10): #defalt start=0, step=1
    print(i)

for i in range(10,12): #defalt step=1
    print(i)    

for i in range(0,12,2): #range(start,stop,step)
    print(i)    


