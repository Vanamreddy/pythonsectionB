
def String(str,char):
    i=0
    count=0
    while i<len(str):
        if str[i] in char:
            count+=1
        i+=1
    print(count) 
String('chintu','c')
String('baby','b')       