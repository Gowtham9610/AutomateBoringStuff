#Dictionary data types
import pprint

myCat ={'size': 'fat','color': 'gray','disposition': 'loud'}

print(myCat['size'])


bool=[1,2,3]==[1,2,3]

print(bool)


print(myCat.keys())


print(myCat.values())

print(myCat.items())

for v in ['g','o','w']:
    print(myCat.values())


message='it a cold april'

count={}


for char in message:
    count.setdefault(char,0)
    count[char] =count [char]+1

pprint.pprint(count)
