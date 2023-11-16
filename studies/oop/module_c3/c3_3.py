import math
from time import sleep

p = math.trunc(math.fmod(math.fabs(-10000000), 55)+0.3)
print(p)
i = 10
while i != 0:
    i -= 1
    sleep(1)
    print(i)

print('время вышло')
