def collatzconjecture(number):
    if (number % 2 == 0):
        return number // 2
    else:
        return 3 * number + 1

number = int(input('input a number: '))
highest = 0
steps = 1

while True:
    number = collatzconjecture(number)
    if (number > highest):
        highest = number
    if (number == 1):
        print(number)
        print('the highest number is :', highest)
        print('it takes', steps, 'steps to get to 1')
        break
    print(number)
    steps += 1