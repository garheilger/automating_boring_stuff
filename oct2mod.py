#! python3
#  oct2mod.py - Converts UNIX filesystem permissions from integer (octal) numbers to UNIX rwx-symbols
#  Date: 29. January 2020
#  Author: G. Arheilger
#  Version: 0.1

import os

stat_info = os.stat(os.getcwd())

# Get file mode, convert string into octal number and build a substring of last 3 numbers
# TODO remove comment: modeInt = stat_info.st_mode
# TODO remove comment: modeOct = oct(modeInt)
# TODO remoce comment: modeStr = modeOct[4:]

modeStr = '615'

# UNIX file permission dictionary
modes = {
         '0':'---',
         '1':'--x',
         '2':'-w-',
         '3':'-wx',
         '4':'r--',
         '5':'r-x',
         '6':'rw-',
         '7':'rwx'
}

mode = ''
modeList = list()
for i in range(len(modeStr)):
    modeList.append(modes[modeStr[i]])
    mode = mode + '|' + modes[modeStr[i]]
mode = mode + '|'

print('')
print('UNIX permissions (decimal value) ' + modeStr)
print('------------------------------------------------------------------------')
print('UNIX permissions list (User, Group, Other) ', modeList)
print('UNIX permissions for User ', modeList[0])
print('UNIX permissions for Group ', modeList[1])
print('UNIX permissions for All others ', modeList[2])
print('UNIX permissions as formatted string ' + mode)