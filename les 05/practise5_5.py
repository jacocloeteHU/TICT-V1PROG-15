
def gemiddelde():
    zin = input('Vul een zin in?:')
    number = 0.0
    tel = zin.split(' ')
    for woord in zin:
        number = number + len(woord)
    print(number)

    gem = number / len(tel)


    return gem

print(gemiddelde())
