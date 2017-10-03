try:
    aantal = eval(input('Met hoeveel personen ben je?'))
    print(aantal)

    if(aantal < 0):
        raise ValueError
    elif(type(aantal) == 'str'):
        print('str')
    bedrag = 4356 / aantal
    print(bedrag)
except ZeroDivisionError:
    print('Kan niet delen door nul')

except ValueError:
    print('Negatieve getallen zijn niet toegestaan!')
except NameError:
    print('Gebruik cijfers voor het invoeren van het aantal!')

except:
    print('Onjuiste invoer!')
