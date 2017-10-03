import random

dubbel = 0

def monopolyworp():
    randomDictionary  = {'db1' : random.randrange(1,7), 'db2' : random.randrange(1,7)}
    return randomDictionary

while dubbel < 3:
    dices = monopolyworp()
    total = dices['db1'] + dices['db2']

    if(dices['db1'] == dices['db2'] and dubbel < 2):
        print('{} + {} = {} (dubbel)'.format( dices['db1'],dices['db2'], total))
        dubbel +=1
    elif(dices['db1'] == dices['db2'] and dubbel < 3):
        print('{} + {} = {} (direct naar gevangenis)'.format( dices['db1'],dices['db2'], total))
        dubbel +=1
    else :
        print('{} + {} = {} '.format( dices['db1'],dices['db2'], total))
        dubbel = 0
