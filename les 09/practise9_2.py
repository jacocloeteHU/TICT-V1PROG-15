import datetime
import csv
bestand = 'inloggers.csv'
#gebruik hier een herhalingslus:
naam = input("Wat is je achternaam? ")
voorl = input("Wat zijn je voorletters? ")
gbdatum = input("Wat is je geboortedatum? ")
email = input("Wat is je e-mail adres? ")
#wanneer de volgende persoon inlogt is onbekend, dus schrijf meteen naar file

with open('newfile.csv', 'a', newline='') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=';')


    writer.writerow((naam, voorl,gbdatum, email))
