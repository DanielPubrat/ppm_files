from itertools import batched

inputFile = open("blocks.ppm")
aList = []


'''MODULE 1:
Setting up the list.
Each line in the file is seperated into groups of 3 RGB values saved as tuples.'''

for line in inputFile:
    aList.append(line)

for i in aList[1:2]:
    dimensions = i.split()
    print (dimensions)

index = 2
for i in aList[2:]:
    aList[index] = i.split()
    index += 1

tempList = []
index = 3
for i in aList[3:]:
    for j in batched(i, 3):
        tempList.append(j)
    aList[index] = tempList
    tempList = []
    index += 1

'''MODULE 2:
Exporting the list'''

def export():
    index = 0
    exportString = ""
    for line in aList:
        for tuple in line:
            for value in tuple:
                exportString += value
                if line in aList[3:]:
                    exportString += " "
        if index >= 2:
            exportString += "\n"
        index += 1
    f = open("export.ppm", "r+")
    f.write(exportString)

    print(f.read())
    f.close()

export()