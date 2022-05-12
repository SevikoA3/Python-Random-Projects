import random
import os

choices = ['rock', 'paper', 'scissor']

loop = False
while True :
    if (loop == True) :
        conAnswer = input('do you want to continue playing?(y/n)\n')
        if (conAnswer == 'n') :
            break
        elif (conAnswer == 'y'):
            pass
            os.system('cls')
        else :
            print('press y or n')
            continue
    
    
    answer = int(input('choose your champion.\nrock[1], paper[2], scissor[3]\n'))-1
    randAns = random.randint(0,2)
    print('the computer chooses ' + choices[randAns] + '.')
    if (answer == 0) :
        if (randAns == 0) :
            print('draw, so close!')
        elif (randAns == 1) :
            print('the computer win, you lose!')
        elif (randAns == 2) :
            print('you win')
    elif (answer == 1) :
        if (randAns == 0) :
            print('you win!')
        elif (randAns == 1) :
            print('draw, so close!')
        elif (randAns == 2) :
            print('the computer win, you lose!')
    elif (answer == 2) :
        if (randAns == 0) :
            print('the computer win, you lose!')
        elif (randAns == 1) :
            print('you win')
        elif (randAns == 2) :
            print('draw, so close!')
    
    loop = True