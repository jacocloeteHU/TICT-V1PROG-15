nullingevoerd = False
getallen = []
while(nullingevoerd == False):
    getal = eval(input('Geef een getal: '))
    if(getal == 0):
        nullingevoerd = True
        print('Er zijn {} getallen ingevoerd, de som is: {}'.format(len(getallen), sum(getallen)))

    else:
        getallen.append(getal)
