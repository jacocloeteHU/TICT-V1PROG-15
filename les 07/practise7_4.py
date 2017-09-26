def ticker(filename):
    infile = open(filename,'r')
    lines = infile.readlines()
    infile.close()
    dic = {}
    for line in lines:
        line = line.strip()
        line = line.split(':')
        dic[line[0]] = line[1]
    return dic

print(ticker('tickerSymbols.txt'))
dictionary = ticker('tickerSymbols.txt')

company = input('Enter Company name: ')
print('Ticker symbol: {}\n'.format(dictionary[company]))
Ticker = input('Enter Ticker symbol: ')
for key, value in dictionary.items():
    if value ==  Ticker:
        print('Company name: {}'.format(key))
