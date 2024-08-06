# index of list is from 0 to positive direction from left the right 
# and from -1 to negative direction from right to left


#lists
    # lists are mutable {we can change the value of the lists}
marks=[1,"yahya",3,4,5]#it can contain haterogenus data type
print(marks)

print(marks[0])
print(marks[1])

print(len(marks))

#slicing on lists
print(marks[1:4])#it include least index and exclude greater index
print(marks[:])
print(marks[-3:-1])#it include least index and exclude greater index


#list methods which return None and work on original list
listx=[1,2,3,4,5]
listc=['a','b','c','d','e']

listx.append(0)#it append new elements in the list
print(listx)

listx.sort()
print(listx)
listc.sort()
print(listc)

listx.sort(reverse=True)
print(listx)
listc.sort(reverse=True)
print(listc)

listx.reverse()
print(listx)

listx.insert(2,"yahya")#it modify the list, first paremetere is index and second is new element
print(listx)

listx.remove(1)#it remove element equal to the input number
print(listx)

listx.pop(0)#it remove the element at the input index value
print(listx)


#tuples
    #tuples are immutable like string i.e. it's values does't change

tu=()#empty tuple

tup=(1,2,3)
print(tup)

tup1=(1,)#for single value tuple comma is necessary because tup1=(1) means assigining value 1 to a variable tup1
print(tup1)

print(tup[0:2])#slicing ln tuples

print(tup.index(3))#it return the first index value of the input element

print(tup.count(1))#it return the total number of occurence of input elements