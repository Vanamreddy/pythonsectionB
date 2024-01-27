a=input('enter a string')
i=-1
while i>=-len(a):
 if a[i] not in a[:i-1]:
    print(a[i])
    break
 i-=1