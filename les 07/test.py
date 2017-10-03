woorden = ['Hogeschool', 'Utrecht', 'Hogeschool', 'Utrecht', 'Python']
for woord in woorden:

    if woord == 'Utrecht':
        print(woord, end=' ')
    else:
        continue

    print('Hogeschool', end=' ')
# ---------------------------------------------------------------------------

import random

worpen = set()
worps = []
for i in range(0, 20):
    dice = random.randrange(1, 6)
    print(str(dice), end='-')
    worpen.add(dice)
    worps.append(dice)
print(worps)
print(worpen)
# ---------------------------------------------------------------------------------
stations = ['Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal']

# f = open('stations.txt', 'w')

for station in stations[1:2]:
    print(station)
    # f.write(station + '\n')

# f.close()
