a,b=0,1
n=int(input(1))
print(a,end=',')
while b<n:
    print(b,end=',')
    a,b=b,a+b
    