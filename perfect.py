num=int(input('enter number'))
res=0
for k in range(1,num):
    if num%k==0:
        res+=k
if res==num:
    print('perfect number')
else:
    print('not perfect number')            