def rev_vowels(st):
    temp=''
    for i in st:
        if i in 'aeiouAEIOU':
            temp+=i
            out=''
            j=-1
    for k in st:
        if k in 'aeiouAEIOU':
            out+=temp[j]
            j+=1
    else:
        out+=k
    return out 
print(rev_vowels('hello'))             
    
            



