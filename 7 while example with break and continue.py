#while example with break and continue



name='bob'
spam=0
while True:
    print('Enter the user name')
    newname=input()
    if newname == name:
        print('u are the valid user')
        break



while spam<5:
    spam=spam+1
    if spam==3:
        continue
    print('this is spam' + str(spam))

print('Program Ends')
    
