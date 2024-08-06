#use ' " ''' in strings {eg:"what's your name" (as in the case of apostrophes)}
#strings are immutable ie.. it cannot be changed
#string index counted from 0 to the positive direction from left to right
#but in string index is counted from -1 to the negative direction from right to left


str1="mohammed "
str2="yahya"
print(str1+str2)

print(len(str1))

print(str1[0])#to access string elements but manuplation is not allowed
print(str1[1])#to access string elements but manuplation is not allowed

print(str1[0:5])#this is called slicing of string 
print(str1[:len(str1)])#in slicing last index does't include
print(str1[:])#print whole string

#as strings are immutable therefore it return new string on manuplation
print(str1.endswith("ed "))#it return True if the str1 is end with "ed "
print(str1.capitalize())#it return string capitalize first character of an string
print(str1.replace("m","n"))#it return string replace all (old) "m" in string by (new)"n"
print(str1.find("moh"))#it return index value of the first char wich mach the given string and if it is negative the string not found
print(str1.count("m"))#it return number of occurence of input element of string 