infile = open('kaartnummers.txt', 'r')

content =  infile.readlines()
infile.close()
contentLength = len(content)
num = 0
locatie = 0
for row in range(0,contentLength,1):
    items = content[row].split(',')
    lastItem = eval(items[0])

    if lastItem >= num:
        num = lastItem
        locatie = row+1

print('Deze file telt {} regels'.format(contentLength))
print('Het grootste kaartnummer is: {} en dat staat op regel {}'.format(num, locatie))
