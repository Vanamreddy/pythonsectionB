class kuttyError(Exception):
    pass
name = input('enter a name :-')
if len(name)<=4:
    raise kuttyError(f'name should be more than 4 characters but{len(name)}were given')
else:
    print('name is validated')