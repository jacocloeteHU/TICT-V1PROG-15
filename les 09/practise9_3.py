
import csv
with open('gamersfile.csv', 'r') as myCSVFile:

    reader = csv.reader(myCSVFile, delimiter=';')
    score = ['','','0']
    for row in reader:
        if eval(score[2]) < eval(row[2]):
            score = row
    print('De hoogste score is: {} op {} behaald door {}'.format(score[2],score[1],score[0]))
