infile = open('kaartnummers.txt', 'r')
content = infile.readlines()

infile.close()

outfile = open('kaartnummersuit.txt', 'w')


for row in content:
    brokenString =  row.split(',')
    numbers = brokenString[0]
    names = brokenString[1].strip()     #.replace('\n', "")
    print('{} heeft kaartnummer: {}'.format(names, numbers))
    outfile.write('{} heeft kaartnumer: {}\n'.format(names, numbers))
outfile.close()
