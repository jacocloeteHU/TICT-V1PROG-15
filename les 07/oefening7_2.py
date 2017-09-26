week = { 'ma' : 'maandag', 'di' : 'dinsdag', 'wo' : 'woensdag', 'do' : 'donderdag', 'vr' : 'vrijdag'}
print(week['ma'])
print('ma' in week)
week['za'] =  'zaterdag'
print(week)

for key in week.keys():
    print(key)
for key in week.values():
    print(key)
for key in week.items():
    print(key)
for key in week:
    print(key)
