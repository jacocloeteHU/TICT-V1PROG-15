import xmltodict

def processXML(filename):
    with open(filename) as myXMLFile:
        filecontentstring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filecontentstring)
        return xmldictionary

artikelendict = processXML('artikels.xml')
artikelen = artikelendict['artikelen']['artikel']

for artikel in artikelen:
    print(artikel['naam'])
