#!/usr/bin/python

import sys
import re

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

class Cave:
    def __init__(self):
        self.cave = [['.']]
        self.topLeftX = 500
        self.botomY = 0
        self.cW = 1
        self.cH = 1

    def getXY(self, x, y):
        newX = x-self.topLeftX
        newY = y
        return (newX, newY)

    def resizeX(self, nextX):
        if nextX < self.topLeftX:
            newCave = []
            for row in self.cave:
                newCave.append(['.' for x in range(self.topLeftX - nextX)])
                newCave[-1] += row

            self.cW += (self.topLeftX - nextX)
            self.topLeftX = nextX
            self.cave = newCave

        elif nextX >= (self.topLeftX + self.cW):
            newCave = []
            for row in self.cave:
                newCave.append(['.' for x in range(nextX - (self.topLeftX + self.cW)+1)])
                newCave[-1] = row + newCave[-1]

            self.cW += (nextX - (self.topLeftX + self.cW)+1)
            self.cave = newCave

    def resizeY(self, nextY):
        if nextY >= self.cH:
            for i in range(nextY-self.cH+1):
                self.cave.append(['.' for x in range(len(self.cave[0]))])

            self.cH = nextY + 1

    # x and y are already in cave space
    # return = next value, -1,-1 is abyss
    def sandNextPos(self, x, y):
        self.resizeX(x)
        (xIdx, yIdx) = c.getXY(x,y)

        if yIdx == self.cH:     return (-1,-1)
        if (yIdx+1) == self.cH: return (-1,-1)

        if self.cave[yIdx+1][xIdx] == '.': return (x, y+1)
        if self.cave[yIdx+1][xIdx] in ['#', 'o']:
            if   self.cave[yIdx+1][xIdx-1] == '.': return (x-1, y+1)
            elif self.cave[yIdx+1][xIdx+1] == '.': return (x+1, y+1)
            else:                                  return (x,   y)


inputFile = open(sys.argv[1], "r")
paths = []
for line in inputFile.readlines():
    line = line.rstrip()
    prevPt = None
    lastFound = False
    while not lastFound:
        rePt     = re.match('^(\d+),(\d+) -> ', line)
        rePtLast = re.match('^(\d+),(\d+)$',   line)

        if rePt:
            line = re.sub('^(\d+),(\d+) -> ','', line)
            newPt = (int(rePt.group(1)), int(rePt.group(2)))
        if rePtLast:
            line = re.sub('^(\d+),(\d+)$','', line)
            newPt = (int(rePtLast.group(1)), int(rePtLast.group(2)))
            lastFound = True

        if prevPt:
            paths.append([prevPt, newPt])

        prevPt = newPt

c = Cave()

for p in paths:
    minX = min(p[0][0], p[1][0])
    maxX = max(p[0][0], p[1][0])
    minY = min(p[0][1], p[1][1])
    maxY = max(p[0][1], p[1][1])
    for x in range(minX, maxX+1):
        for y in range(minY, maxY+1):
            c.resizeX(x)
            c.resizeY(y)

            (nX, nY) = c.getXY(x,y)
            c.cave[nY][nX] = '#'

for row in c.cave:
    print("".join(row))
print(c.cW, 'x', c.cH)



print("------------------")
print("---- PART 1 ------")
print("------------------")
inAbyss=False
units = 0
while not inAbyss:
    moved = True
    sand = (500,0)

    while moved and not inAbyss:
        print(sand)
        sandNxt = c.sandNextPos(sand[0], sand[1])
        
        if sandNxt == sand:
            (nX, nY) = c.getXY(sand[0], sand[1])
            c.cave[nY][nX] = 'o'
            moved=False

        if sandNxt == (-1,-1):
            inAbyss = True

        sand = sandNxt
    
    print('-----------------------------------------------------------')
    for row in c.cave:
        print("".join(row))

    units += 1

print(f'Units = {units-1}')

quit()

print("------------------")
print("---- PART 2 ------")
print("------------------")




