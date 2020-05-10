# sample program for try and except

def divide42by(val):
    try:
        print(42/val)
    except ZeroDivisionError:
            print('never divide a number with zero')


divide42by(2)
divide42by(4)
divide42by(0)
divide42by(1)


print('Enter the number from 1 to 6')
num=int(input())
try:
    if num==5:
        print('you are the winner')
    else:
        print('better luck next time')
except:
    print('Enter the valid value')

print('Program Ends')






