import random

dots = int(input('how many dots do you want?\n'))

circle = 0
square = 0
for i in range(dots) :
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    if x**2 + y**2 <= 1 :
        circle += 1
    square += 1

print('estimation of pi from', dots, 'dots:', 4*circle/square)