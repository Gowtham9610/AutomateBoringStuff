#guess number game
import random
print('Enter your name')
name=input()
print('Hi ' +name+' welcome to the Guess number game, I am thinking of a number from 1 to 20, Guess it')
secretnumber= random.randint(1,20)


for guesstaken in range(1,6):
    print('Enter the number')
    guessnumber=int(input())
    if guessnumber > secretnumber:
        print('your guess is too high')
    elif guessnumber <secretnumber:
        print('your guess is too low')
    else:
        break

if guessnumber == secretnumber:
    print('you have guessed the number correctly')
else:
    print('your chance is over'+str(guesstaken)+ ', Thanks for playing, better luck next time')

