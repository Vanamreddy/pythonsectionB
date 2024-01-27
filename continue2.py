sum=0
sum1=0
a=(1,2,3,6,8,9,12,15)
i=0
while i<len(a):
    if a[i]%2==0:
        sum+=a[i]
        i+=1
        continue
    if a[i]%3==0:
        sum1+=a[i]
        i+=1
        continue
    i+=1
print(sum,sum1)        