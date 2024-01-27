import re

with open(r"C:\Users\Administrator\Desktop\lorem.txt",'r+',encoding='utf-8') as file:
    data = file.read()
    newdata=re.sub(' ','_',data)
    file.seek(0)
    file.write(newdata)