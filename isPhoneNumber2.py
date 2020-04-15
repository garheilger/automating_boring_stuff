"""
    isPhoneNumber(text)

    Return value: text

    Programmiert unter Verwendung regulärer Ausdrücke.
"""

# Python Bibliotheken importieren
import re

def isPhoneNumber(text):

    # Mit den runden Klammern innerhalb des regulären Ausdrucks, lassen sich Gruppen bilden,
    # die mit Hilfe der .group()-Methode einzeln angesprochen und bearbeitet werden können.
    phoneNumberRegexUS = re.compile(r'(\d{3})?-(\d{3}-\d{4})')
    matchedObjects = phoneNumberRegexUS.search(text)

    # Mit Hilfe der .group()-Methode werden Area-Code und Rufnummer separat angesprochen
    phoneNumber = matchedObjects.group()
    areaCode = matchedObjects.group(1)
    mainNumber = matchedObjects.group(2)

    # Wir geben eine Liste mit folgender Reihenfolge zurück:
    # Element 0: Gesamte Rufnummer
    # Element 1: Area Code
    # Element 2: Rufnummer
    phoneNumberList = [phoneNumber, areaCode, mainNumber]

    return phoneNumberList

phoneNumber = []
phoneNumber = isPhoneNumber('My number is 415-555-4242.')

print('')
print('Vollständige Telefonnummer: ' + phoneNumber[0])
print('Area code.................: ' + phoneNumber[1])
print('Telefonnummer.............: ' + phoneNumber[2])




