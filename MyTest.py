#! python3

import re

#   ? 0 or 1
#   * 0 or more
#   + 1 or more
#   . universal character match
#   \s  whitespace
#   \S  not whitespace
#   \d  digit
#   \D  not digit
#   \w  word
#   \W  not word
#   ^   beginning of line
#   $   end of line
#   [0-9]   same as \d
#   [^0-9]  same as \D

try:
    fhandle = open(r'c:\Users\WGeorg\Downloads\copybook.txt')
except:
    print('Problem opening file...')
    exit()

rowCount = 0

for line in fhandle:
    rowCount += 1
    print(line)

print(str(rowCount))
