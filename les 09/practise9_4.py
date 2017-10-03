import csv


headers = ['Artikelnummer','Artikelcode','Naam','Voorraad','Prijs']
artikelen = [[121,'ABC123','Hightlight pen',231,0.56],
 [123,'PQR678','Nietmachine',587,9.99],
[128,'ZYX163','Bureaulamp',34,19.95],
[137,'MLK709','Monitorstandaard',66,32.50],
[271,'TRS665','Ipad hoes',155,19.01]]

with open('artikels.csv', 'w', newline='') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=';')
    writer.writerow(headers)
    for row in artikelen:
        writer.writerow(row)

with open('artikels.csv', 'r') as myCSVFile:

    reader = csv.DictReader(myCSVFile, delimiter=';')
    prijs = {'Prijs' : '0'}
    voorraad = {'Voorraad' : '9999999999'}
    totaalvoorraad = 0
    for row in reader:

        if( eval(row['Prijs']) > eval(prijs['Prijs'])):
            prijs = row
        elif(eval(row['Voorraad']) < eval(voorraad['Voorraad'])):
            voorraad = row
        totaalvoorraad += eval(row['Voorraad'])

    print('Het duurste artikel is {} en die kost {} Euro'.format(prijs['Naam'],prijs['Prijs']))
    print('Er zijn slechts {} exemplaren in voorraad van het product met nummer {}'.format(voorraad['Voorraad'],voorraad['Artikelnummer']))
    print('In totaal hebben wij {} producten in ons magazijn liggen'.format(totaalvoorraad))
