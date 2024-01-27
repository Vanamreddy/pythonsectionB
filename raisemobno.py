
class phoneNumberError(Exception):
    pass
number = input('enter a number :-')
if len(number)!=10:
    raise phoneNumberError(f'number should be consist of 10 digits {len(number)} were given')
else:
    print('number is validated')