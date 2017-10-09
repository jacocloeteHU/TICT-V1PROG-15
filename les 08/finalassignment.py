
def inlezen_beginstation(stations):
    while True:
        beginstation = input('Wat is je beginstation?')
        if(beginstation in stations):
            break
    return beginstation


def inlezen_eindstation(stations, beginstation):
    while True:
        eindstation = input('Wat is je eindstation?')
        if(eindstation in stations):
            indexEindstation = stations.index(eindstation)
            indexBeginstation = stations.index(beginstation)
            if(indexEindstation > indexBeginstation):
                break
            else:
                print('Deze trein komt niet in {}'.format(eindstation))
    return eindstation

def omroepen_reis(stations, beginstation, eindstation):
    indexEindstation = stations.index(eindstation)
    indexBeginstation = stations.index(beginstation)
    verschil = indexEindstation - indexBeginstation
    bedrag = 5 * verschil
    print('Het beginstation {} is het {}e station in het traject.'.format(beginstation, indexBeginstation))
    print('Het eindstation {} is het {}e station in het traject.'.format(eindstation,indexEindstation))
    print('De afstand bedraagt {} station(s)'.format(verschil))
    print('De prijs van het kaartje is {} euro'.format(bedrag))

    print('Jij stapt in de trein in: {}'.format(beginstation))
    for i in range(indexBeginstation + 1,indexEindstation):
        print('- {}'.format(stations[i]))
    print('Jij stapt uit in: {}'.format(eindstation))


stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', "’s-Hertogenbosch", 'Eindhoven', 'Weert','Roermond', 'Sittard','Maastricht' ]

beginstation = inlezen_beginstation(stations)
print(beginstation)
eindstation = inlezen_eindstation(stations, beginstation)
print(eindstation)
omroepen_reis(stations, beginstation, eindstation)
