def st(a):
    out=[]               
    for char in st:
        if char in st:
            out[char]+=1
        else:
            out[char]=1
    return out
print(st(['abcd',[1,2,3]]))       