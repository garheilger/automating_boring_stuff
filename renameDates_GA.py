#!  python3
#   renameDates_GA.py - Ändert amerikanische MM-DD-YYYY-Angaben in Dateinamen in europäische
#   DD-MM-YYYY-Datumsangaben
#

import shutil, os, re

# Regulärer Ausdruck für Dateinamen mit Datumsangaben im US-Format
datePattern = re.compile(r"""^(.*?)     # Gesamter Text vor dem Datum
    ((0|1)?\d)-                         # Ein oder zwei Ziffern für den Monat
    ((0|1|2|3)?\d)-                     # Ein oder zwei Ziffern für den Tag
    ((19|20)\d\d)                       # Vier Ziffern für das Jahr
    (.*?)$                              # Gesamter Text nach dem Datum
""", re.VERBOSE)

# Alle Dateien im Arbeitsverzeichnis durchlaufen
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    # Dateinamen ohne Datumsangaben überspringen
    if mo == None:
        continue

    # Die einzelnen Teile des Dateinamens abrufen
    beforePart = mo.group(1)
    monthPart  = mo.group(2)
    dayPart    = mo.group(4)
    yearPart   = mo.group(6)
    afterPart  = mo.group(8)

    # Dateinamen im europäischen Format zusammenstellen
    euroFilename = beforePart + yearPart + '-' + monthPart + '-' + dayPart + '_' + afterPart

    # Den kompletten absoluten Pfad abrufen
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # Dateien umbenennen
    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))

    # TODO: Nach dem Test entkommentieren
    # shutil.move(amerFilename, euroFilename)