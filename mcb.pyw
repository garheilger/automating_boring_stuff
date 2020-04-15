#! python3
#  ncb.pyw - Speichert Text und lädt ihn in die Zwischenablage
#  Verwendung: python mcb.pyw save <Schlüssel> - Speichert den Inhalt in der Zwischenablage unter dem Schlüssel
#              python mcb.pyw <Schlüssel>      - Lädt den Wert zu dem Schlüssel in die Zwischenablage
#              python mcb.pyw list             - Lädt alle Schlüsselwörter in die Zwischenablage

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Speicher den Inhalt der Zwischenablage
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # Schlüsselwörter auflisten und Inhalt laden
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()

