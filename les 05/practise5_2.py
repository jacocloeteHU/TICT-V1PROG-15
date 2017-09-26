infile = open('kaartnummers.txt', 'r')
content = infile.readlines()

infile.close()

for row in content:
    brokenString =  row.split(',')
    numbers = brokenString[0]
    names = brokenString[1].strip()     #.replace('\n', "")
    print('{} heeft kaartnummer: {}'.format(names, numbers))


