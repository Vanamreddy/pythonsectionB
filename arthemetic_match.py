a =int( input('enter a number 1 :-'))
b =int( input('enter a number 2 :-' ))
c=( input('enter operator :-'))
match c:
    case '+':
        print(a+b)
    case '-':
        print(a-b)
    case '*':
        print(a*b) 
    case '**':
        print(a**b)
    case '/':
        print(a/b)
    case '//':
        print(a//b)
    case '%':
        print(a%b)
    case _:
        print('enter valid input')              