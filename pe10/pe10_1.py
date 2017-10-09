import xmltodict

def processXML(filename):
    with open(filename) as myXMLFile:
        filecontentstring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filecontentstring)
        return xmldictionary

voorbeeldendict = processXML('Artikelen.xml')
voorbeelden = voorbeeldendict['artikelen']['artikel']

for voorbeeld in voorbeelden:
    print(voorbeeld['naam'])