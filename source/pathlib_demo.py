#! python3
# Demonstration von Funktionen des pathlib-Moduls
#

import grp
import pwd
import os

from pathlib import Path
from os.path import join, getsize

stat_info = os.stat(os.getcwd())
uid = stat_info.st_uid
gid = stat_info.st_gid

# Zugriffsrechte ermitteln, in Oktalzahl umwandeln und anschliessend die führenden Zeichen '0o' entfernen
mode = oct(stat_info.st_mode).lstrip('0o')

print()
print('grp, pwd, os Beispiel')
print('=====================================')
print('Verzeichnis: ', os.getcwd())
print('User-Id..: ', uid)
print('Group-Id.: ', gid)
print()

user = pwd.getpwuid(uid)[0]
group = grp.getgrgid(gid)[0]
print('=====================================')
print('User.....: ', user)
print('Group....: ', group)
print()

print('Pathlib-Beispiel')
print('=====================================')
thisPath = Path("/Users/garheilger/Documents/100 Development/001 Repositories/Automating_the_boring_stuff")
if thisPath.exists():
    print('Owner: ', thisPath.owner())
    print('Group: ', thisPath.group())

print('')
print('Demo 1 of os.walk()')
print('=====================================')
print('')
for root, dirs, files in os.walk(os.getcwd()):
    print(root, "consumes", end=" ")
    print(sum(getsize(join(root, name)) for name in files), end=" ")
    print("bytes in", len(files), "non-directory files")

print('')
print('Demo 2 of os.walk()')
print('=====================================')
print('')
for folderName, subfolders, filenames in os.walk(os.getcwd()):
    print('Current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)
    print('')

print('')
print('Done!')
print('')