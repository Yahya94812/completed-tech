import sys
import string
import os.path

fname=input("enter the file name or path :")
if not os.path.isfile(fname):
    print(fname,"does't exist")
    sys.exit(0)

infile=open(fname,"r")
filecontents=""
for line in infile:
    for ch in line:
        if ch not in string.punctuation:
            filecontents=filecontents+ch
        else:
            filecontents=filecontents+""     

wordfreq={}
wordlist=filecontents.split()
for word in wordlist:
    if word not in wordfreq.keys():
        wordfreq[word]=1
    else:
        wordfreq[word]+=1

sortedwordfreq=sorted(wordfreq.items(),key=lambda x:x[1],reverse=True)

for i in range(10):
    print(sortedwordfreq[i][0]," occured in ",sortedwordfreq[i][1]," times")
# print(wordfreq)
# print(filecontents)