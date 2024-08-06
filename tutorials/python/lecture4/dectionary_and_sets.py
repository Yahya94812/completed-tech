#dectionary
#it is unorderd and mutable data structure and not contain any duplicate key
#it contain key and value seprated by {:}
#key is any immutable data type e.g.. strings,tuples,int etc
#but the value maybe any data type including mutable data type e.g.. list,dictionary


dec={
    "key":"value", 
    "name":"yahya",
    "class":2,
    "old":False,
    "marks":[1,2,3,4,5],
    (1,2,3,4,5):[1,2,3,4,5]
    }

print(dec)    
print(dec["old"])
print(dec["marks"])
dec["old"]=True  #you can modify by assinging the new value
print(dec["old"])

dec["young"]=False #you can creat a new element in dictionary
print(dec)

null_dict={} #you can creat a null dictionary
print(null_dict)

stu={
    "name":"yahya",
    "marks":{
        "eng":12,
        "kann":21
    }
    }

print(stu["name"])
print(stu["marks"]["eng"])    

#methods in dictionary
abc={
    "a":1,
    "b":2,
    "c":3
}

print(abc.keys())#printing all the keys of dictionary
print(list(abc.keys()))#printing all the keys of dictionary in list data type

print(abc.values())#printing all the values of dictionary as a tuple
print(list(abc.values()))#printing all the values of dictionary in list data type

print(abc.items())#it return all items in dictionary in tuple data type

print(abc.get("a"))#return value at the key "a" and retutn None (insted of error) if the input does't exist as a key

abc.update({"d":4})#for adding new elements in dictionary
print(abc)
abc.update({"d":1})
print(abc)#for modifying dictionary
new_dec={"e":5}
abc.update(new_dec)
print(abc)#for modifying dictionary



#sets
#sets it self are mutable but it's elements are immutable therefore list and dictionary cannot stored as its elements
#it is unorderd and it is uniqe

se={1,2,3,4,4}
print(len(se))#duplicate elements are ignored

null_set=set()#exception for creating null set because null_set={} creat a null dictionary
print(len(null_set))

#methods in sets

setx={1,2,3,4,5,"yahya"}

setx.add(8)#it add only one element to the given set
print(setx)

setx.remove(1)#it remove only one element from a set
print(setx)

print(setx.pop())# (doubt)it remove random value from a set
print(setx)

setx.clear()#it clear the all element in the set
print(setx)

seta={1,2,3,4,5}
setb={5,6,7,8,9}

print(seta.union(setb))#it return the union of the two sets without effecting the sets
print(seta)#uneffected
print(setb)#uneffected

print(seta.intersection(setb))#it return the intersection of the two sets without effecting the sets
print(seta)#uneffected
print(setb)#uneffected

sete={9,9.0}#exception
print(sete)#print only 9