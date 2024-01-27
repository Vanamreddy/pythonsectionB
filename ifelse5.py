x=eval(input('enter value of x:'))
if type(x)in(bool,int,float,complex):
    print(x**2)
else:
    print(3*len(x)+1)