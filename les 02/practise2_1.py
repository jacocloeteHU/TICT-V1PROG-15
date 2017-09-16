# 2_1
letters = ('A', 'C', 'B', 'B', 'C','A', 'C', 'C', 'B')
alfabet  = ('A', 'B', 'C')
newArr = []
for char in alfabet :
    p = letters.count(char)
    newArr.append(p)

print(newArr)
# list = [letters.count('A'),letters.count('B'),letters.count('C')]
