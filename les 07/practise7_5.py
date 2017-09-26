def namen():
    dictonary = {}
    while(True):
        naam = input('Volgende naam: ')
        if(naam == ''):
            break
        else:
            if(naam not in dictonary):
                dictonary[naam] = 1
            else:
                dictonary[naam] += 1
    for name, waarde in dictonary.items():
        if(waarde > 1):
            print('Er zijn {} studenten met de naam {}'.format(waarde,name))
        else:
            print('Er is {} student me de naam {}'.format(waarde,name))


namen()
