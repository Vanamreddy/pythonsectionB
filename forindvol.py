a='good morning'
i=0
out=[]
for i in range(len(a)):
    if a[i] in 'aeiouAEIOU':
        out+=[i]
print(out)