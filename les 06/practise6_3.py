invoer = '5-9-7-1-7-8-3-2-4-8-7-9'
list = invoer.split('-')

newList = []
for row in list:
    newList.append( eval(row))
list = newList
list.sort()

print('Gesorteerde list van ints : {}'.format(list))
print('Grootste getal: {} en Kleinste getal: {}'.format(max(list),min(list)))
print('Aantal getallen {} en Som van de getallen: {}'.format(len(list), sum(list)))
print('Gemiddelde: {:3.2f}'.format(sum(list)/len(list)))
