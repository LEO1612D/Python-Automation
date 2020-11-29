import re

data = open("test-demo.txt","r")

# result = re.findall(r"^\.[ \W]",data.readline())

# print(result)


content=data.readline().split('.')

newData = ""
for i in content:
    newData = newData+i+"\n\n"


newFile = open("automated.txt","w+")

newFile.write(newData)