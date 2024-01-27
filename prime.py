num=int(input('enter a number'))
i=1
count=0
while i<=num:
    if num%2==0:
        count+=1
    i+=1
if count==2:        
    print('prime')
else:
    print('not prime')
