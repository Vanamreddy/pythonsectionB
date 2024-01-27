b=[2,8,6,4,3,23,2,1,8,9]
print(list(map(lambda b:b**2, b)))
print(list(map(lambda b:b**3,filter(lambda b:b%2==0 ,b))))

