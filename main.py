import itertools
from itertools import batched
import numpy

'''MODULE 1:
Setting up the list.
Each line in the file is seperated into groups of 3 RGB values saved as tuples.'''

class PPMimage():

    def set_to_3d_list(self):
        self.startingNums = self.aList[:3]
        #print(self.startingNums)
        self.aList = self.aList[3:]
        #self.aList = numpy.array(self.aList)
       # self.aList = self.aList.reshape(3, int(self.startingNums[1]), int(self.startingNums[2]))
       # self.aList = list(self.aList)
        
        tempList = []
        index = 0
        for line in self.aList:
            for group in batched(line, 3):
                tempList2 = []
                for item in group:
                    tempList2.append(item)
                tempList.append(tempList2)
            self.aList[index] = tempList
            tempList = []
            index += 1

    def __init__(self, inputFile, exportFile):
        self.inputFile = open(inputFile)
        self.exportFile = exportFile
        self.aList = []
        self.lengths = []

        lineList = []
        for line in self.inputFile:
            line = line.strip().split(' ')
            self.lengths.append(len(line))
            for val in line:
                lineList.append(val)
            self.aList.append(lineList)
            lineList = []
    
        self.lengths = self.lengths[3:]

       # print (self.lengths)

        self.set_to_3d_list()
        
    '''MODULE 2:
    Exporting the list'''

    def export(self):

        with open(self.exportFile,'w') as file:
            pass

        index = 0
        length = 0
        self.exportString = self.startingNums[0][0] + "\n" + self.startingNums[1][0] + " " + self.startingNums[1][1] + "\n" + self.startingNums[2][0] + "\n"
        for line in self.aList:
            for tuple in line:
                for val in tuple:
                    self.exportString += str(val)
                    self.exportString += " "
                    length += 1
                    if length >= self.lengths[index]:
                        self.exportString += "\n"
                        length = 0
                        if index < 144:
                            index += 1
        f = open(self.exportFile, "r+")
        f.write(self.exportString)
        print(f.read())
        f.close()
        print("exported")

    '''MODULE 3:
    Filters'''

    def negate_red(self):
        for line in self.aList:
            for tuple in line:
                for value in tuple[3:-1:3]:
                    value = str(255 - int(value))
    
        print ("negated red successfully.")

    def flip_horizontal(self):

        self.aList.reverse()

        print ("flipped horizontally.")

    def gray_scale(self):
        tempSum = 0
        for line in self.aList:
            for tuple in line:
                for i in tuple:
                    for j in i:
                        tempSum += int(j)
                tempSum //= 3
                tuple[0] = str(tempSum)
                tuple[1] = str(tempSum)
                tuple[2] = str(tempSum)
        
        print ("gray-scaled successfully.")

    def flatten_red(self):
        for line in self.aList:
            for tuple in line:
                tuple[0] = '0'
        
        print ("flattened red successfully")

r = PPMimage("blocks.ppm", "export.ppm")

#r.negate_red()
#r.flip_horizontal()
#r.gray_scale()
#r.flatten_red()


r.export()
