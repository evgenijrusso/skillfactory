class User:
    pass

peter = User()
peter.name = 'Петр Петрович'
julia = User()
julia.name = 'Юлия Меньшова'
print(peter.name)
print(julia.name)

peter.email = "peterrobertson@mail.com"
print(peter.email)
print('\n')
#print(julia.email)  #AttributeError: 'User' object has no attribute 'email'