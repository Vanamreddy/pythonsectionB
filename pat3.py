rows = int(input('enter no of rows :-'))
for i in range(rows):
    for j in range(rows):
        if i==j or i==rows-j-1:
            print(' ',end='')
        else:
            print('*',end='')
    print()        