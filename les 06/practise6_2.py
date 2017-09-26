list = eval(input('Geef lijst minimaal 10 strings: '))
newList = []

for row in list:
    if(len(row) <= 4):
        newList.append(row)
print(newList)


