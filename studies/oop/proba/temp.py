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


print('------------\n')
DATA_FILL = (
    ("Active", "Активный"),
    ("Inactive", "Неактивный")
)
tup = tuple(x for x in DATA_FILL)
print('tup:', tup)


qw = tuple(t for tup in DATA_FILL for t in tup)
print('qw', qw)

print('проба: ', qw[0], ' ', qw[1], ' ', qw[2])
# for tup in DATA_FILL:
#     for t in tup:
#         print('t:', t)
#
for x in DATA_FILL:
    name0, name1 = x[0], x[1]
    print('name:', name0, 'name1:', name1)
