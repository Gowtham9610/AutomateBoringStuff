# tic tac game using list and dictionary

import random

def printtable():
    print(' '+'|'+' '+'|'+' ')
    print('------')
    print(' '+'|'+' '+'|'+' ')
    print('------')
    print(' '+'|'+' '+'|'+' ')

    

print('*********welcome to Tic-Tac-Toe Game*********')
printtable()

print('''Please select 'x' or 'o' ''')
playerselection=input()
if playerselection=='x':
    print('Your are player one')
    print('Please start the game')
else:
    print('Computer will play first')


print('\
select\n TL - TOP Left,TM - Top Mid,TR - Top Right,\
      \n ML - Mid Left,MM - Mid Middle,MR - Mid Right,\
      \n LL - Low Left,LM - Low Mid,LR - Low Right')
printtable()
selection=input()

dict={'TL':'','TM':'','TR':'','ML':'','MM':'','MR':'','LL':'','LM':'','LR':'',}

