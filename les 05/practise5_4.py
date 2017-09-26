import datetime

def getDate():
    vandaag = datetime.datetime.today()
    s = vandaag.strftime("%a %d %b %Y, %H:%M:%S")
    print(s)
    return s

def write(s):
    infile = open('hardlopers.txt', 'a')
    naam = input('Wie heeft de lijn gepasseert? : ')
    line = s + ", " + naam + "\n"
    infile.write(line)
    infile.close()

    infile = open('hardlopers.txt', 'r')
    contents = infile.readlines()
    print(contents)

    infile.close()
    return len(contents)


registered = 0
while(registered < 5):
    registered = write(getDate())

    print(registered)
