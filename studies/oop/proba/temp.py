# Декораторы
def logging(func):
    def log_function_called():
        print(f'{func}, called.')
    func()
    return log_function_called()

@logging
def my_name():
    print('john')
@logging
def friend_name():
    print('Друг Олег')



