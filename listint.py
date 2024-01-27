a=[9,'9',10,[1,3],'234',12,22.5]
out=[(i,a[i]) for i in range(len(a))   if isinstance(a[i],int)]
print(out)