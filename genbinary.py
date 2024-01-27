def binary(num):
    while num>0:
      yield num%2
      num = num//2
out=''      
for i in binary(10):
   out = str (i)+out
print(out) 
     

