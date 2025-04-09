from itertools import batched

'''MODULE 1:
Setting up the list.
Each line in the file is seperated into groups of 3 RGB values saved as tuples.'''

class PPMimage():
    def __init__(self, inputFile, exportFile):
        self.inputFile = open(inputFile)
        self.exportFile = exportFile
        self.aList = []
        self.lengths = []

        for line in self.inputFile:
            self.aList.append(line)
            self.lengths.append(len(line.split()))

        self.num = self.aList[0]
        for i in self.aList[1:2]:
            self.dimensions = i.split()
            print (self.dimensions)
        
        index = 2
        for i in self.aList[2:]:
            self.aList[index] = i.split()
            index += 1
        
        tempList = []
        index = 3
        for line in self.aList[3:]:
            for group in batched(line, 3):
                tempList2 = []
                for item in group:
                    tempList2.append(item)
                tempList.append(tempList2)
            self.aList[index] = tempList
            tempList = []
            index += 1
        
    '''MODULE 2:
    Exporting the list'''

    def export(self):

        with open(self.exportFile,'w') as file:
            pass

        index = 0
        self.exportString = ""
        for line in self.aList:
            for tuple in line:
                for value in tuple:
                    self.exportString += value
                    if line in self.aList[3:]:
                        self.exportString += " "
            if index >= 2:
                self.exportString += "\n"
            index += 1
        f = open(self.exportFile, "r+")
        f.write(self.exportString)
       # print(f.read())
        f.close()

    '''MODULE 3:
    Filters'''

    def negate_red(self):
        for line in self.aList[3:]:
            for tuple in line:
                tempVal = 255 - int(tuple[0])
                tuple[0] = str(tempVal)
    
        print ("negated red successfully.")

    def flip_horizontal(self):
        tempList = self.aList[:3]
        self.aList = self.aList[3:]
        tempList.reverse()
        for i in tempList:
            self.aList.append(i)
        self.aList.reverse()

        print ("flipped horizontally.")

    def gray_scale(self):
        tempSum = 0
        for line in self.aList[3:]:
            for tuple in line:
                for i in tuple:
                    tempSum += int(i)
                tempSum //= 3
                tuple[0] = str(tempSum)
                tuple[1] = str(tempSum)
                tuple[2] = str(tempSum)
        
        print ("gray-scaled successfully.")

    def flatten_red(self):
        for line in self.aList[3:]:
            for tuple in line:
                tuple[0] = '0'
        
        print ("flattened red successfully")

r = PPMimage("blocks.ppm", "export.ppm")

r.negate_red()
r.flip_horizontal()
r.gray_scale()
r.flatten_red()


r.export()
