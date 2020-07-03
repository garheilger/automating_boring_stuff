#! python3
#
# phoneAndEmail_GA.py - Findet Telefonnummern und E-Mail-Adressen in der Zwischenablage
# 27. Januar 2020
#

import pyperclip, re

# Regulärer Ausdruck für US-Telefonnummern
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # Bereichsvorwahl
    (\s|-|\.)?                      # Trennzeichen
    (\d{3})                         # Erste 3 Stellen
    (\s|-|\.)                       # Trennzeichen
    (\d{4})                         # Letzte 4 Stellen
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # Durchwahl
    )''', re.VERBOSE)

# Regulärer Ausdruck für E-Mail-Adressen
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+               # Benutzername
    @                               # At-Symbol
    [a-zA-Z0-9.-]+                  # Domänenname
    (\.[a-zA-Z]{2,4}){1,2}          # Punkt + irgendetwas
    )''', re.VERBOSE)

# Findet Übereinstimmungen in der Zwischenablage
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Kopiert die Ergebnisse in die Zwischenablage
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found!')
