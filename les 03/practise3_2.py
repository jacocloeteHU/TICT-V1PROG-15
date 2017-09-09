leeftijd = eval(input('Geef je leeftijd:'))
passpoort =  input('Nederlands paspoort:')

if (leeftijd >=  18 and passpoort == 'ja'):
    print('Gefeliciteerd, je mag stemmen!')
else:
    print('Helaas, je mag niet stemmen')
