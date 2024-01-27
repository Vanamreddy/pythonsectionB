def series(n):
    a=1
    for i in range(n):
        yield a
        a=a*2
print(list(series(10)))
        