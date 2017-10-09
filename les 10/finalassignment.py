import xmltodict

def processXML(filename):
    with open(filename) as myXMLFile:
        filecontentstring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filecontentstring)
        return xmldictionary

stationsdict = processXML('stationslijst.xml')
stations = stationsdict['Stations']['Station']

list = []
def spacing():
    return print('')

print('Dit zijn de codes en types van de {} stations:'.format(len(stations)))
for station in stations:

    print('{} - {}'.format(station['Code'],station['Type']))
    if(station['Synoniemen'] != None):
        list.append(station)
spacing()
print('Dit zijn alle stations met één of meer synoniemen:')
for station in list:
    print('{} ->'.format(station['Code']))
    for synoniem in station['Synoniemen']['Synoniem']:
        print('   - {}'.format(synoniem))
        # print('Synoniem: {}'.format(synoniem['Synoniem']))
spacing()
print('Dit is de lange naam van elk station:')
for station in stations:
    print('{} - {}'.format(station['Code'],station['Namen']['Lang']))

