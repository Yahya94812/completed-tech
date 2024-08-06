#modes
#"r"read mode, "w"over write made, "x"creat a file and open it for writing, "a"for writing file in appending mode, "b"binary mode, "t"text mode {default}, "+"open a disk file for updating {writing and reading},"a+" for reading and writing on a file in appending mode,curser is at the same position when we are doing input and output by the single opening of the file, and you can use "rb", "wb" etc for reading and writing in a binary file


f=open("yahya.txt","r") #defalt mode is readmode{"r"} and we can alse use relative path in the place of file name
data=f.read() #it returns data as a string
print(data)
print(type(data))
f.close()

f=open("yahya.txt","r")
data=f.read(5) #it read only 5 char from the present curser
print(data)
f.close()

f=open("yahya.txt","r")
data=f.readline() #it read complete line from the present curser
print(data)
data=f.readline() #does't print any thing because cursor is at the end
print(data)
f.close()


f=open("yahya.txt","w") #all the previus data will be erased {ternucated} and if we use "a" data will not erase
f.write("hello yahoo\n") #we can use \n
f.write("hello yahoo") 
f.close()


with open("yahya.txt","r") as f: #hear f is called alias and by this method file closing is automatically done
    data=f.read()
    print(data)


import os
with open("delet.txt","w") as f: #creating a new file
    f.write("hello")
os.remove("delet.txt") #delet that new file    