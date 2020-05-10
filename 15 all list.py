# all I know about list


print('this is what i Know abot python list')
spam=['hello','this','is','my','list']
print(spam)

print(spam[0])
print(spam.index('hello'))

print(''+str(len(spam)))

print('iterating and indexing list')

#for ite in range(5):
    #print(spam[ite])

#for eta in range(3,5):
    #print(spam[eta])
for gta in [2,4]:
    print(spam[gta])



def addtolist(somelist):
    somelist.append('An')


print('see list is mutable***** so can be changed** it only refers')


addtolist(spam)
print(spam)

spam.insert(4,'gm')

print(spam)





