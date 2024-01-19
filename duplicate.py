a='rohit sharma'
out =' '
for i in range(len(a)):
    if a[i] in a[i+1:]:
        out+= a[i]
print(out)        