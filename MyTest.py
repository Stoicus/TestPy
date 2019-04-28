#! python3

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
