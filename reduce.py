from functools import reduce
b=[1,2,3,4,5]
print(reduce(lambda x,y,:x+y,map(lambda a:a**2,b)))
