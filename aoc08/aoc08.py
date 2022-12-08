#!/usr/bin/python

import sys
import re

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

trees = []
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    row = []
    for t in line.rstrip():
        row.append(int(t))
    trees.append(row)

tHeight = len(trees)
tWidth  = len(trees[0])

visible = []
for i in range(len(trees)):
    vrow = []
    for j in range(len(trees[0])):
        vrow.append(False)

    visible.append(vrow)

for i in range(len(trees)):
    visible[i][0] = True
    visible[i][len(trees[0])-1] = True

for i in range(len(trees[0])):
    visible[0][i] = True
    visible[len(trees)-1][i] = True


print("------------------")
print("---- PART 1 ------")
print("------------------")

# From Right
for y in range(tHeight):
    curMax = 0
    for x in range(tWidth):
        if trees[y][x] > curMax:
            visible[y][x] = True
            curMax = trees[y][x]

# From Left
for y in range(tHeight):
    curMax = 0
    for x in reversed(range(tWidth)):
        if trees[y][x] > curMax:
            visible[y][x] = True
            curMax = trees[y][x]

# From Top
for x in range(tWidth):
    curMax = 0
    for y in range(tHeight):
        if trees[y][x] > curMax:
            visible[y][x] = True
            curMax = trees[y][x]

# From Bottom
for x in range(tWidth):
    curMax = 0
    for y in reversed(range(tHeight)):
        if trees[y][x] > curMax:
            visible[y][x] = True
            curMax = trees[y][x]

vCount = 0
for row in visible:
    for t in row:
        if t: vCount+=1

print(vCount)



print("------------------")
print("---- PART 2 ------")
print("------------------")
maxScore = 0
senic = []
for i in range(len(trees)):
    srow = []
    for j in range(len(trees[0])):
        srow.append(0)
    senic.append(srow)

for y in range(tHeight):
    for x in range(tWidth):
        height = trees[y][x]
        upCnt = 0
        downCnt = 0
        leftCnt = 0
        rightCnt = 0

        # Up
        uPos = y-1
        while uPos > -1:
            upCnt +=1
            if trees[uPos][x] >= height: 
                break
            uPos-=1

        # Down
        dPos = y+1
        while dPos < tHeight:
            downCnt +=1
            if trees[dPos][x] >= height: 
                break
            dPos+=1


        # Left
        lPos = x-1
        while lPos > -1:
            leftCnt +=1
            if trees[y][lPos] >= height: 
                break
            lPos-=1


        # Right
        rPos = x+1
        while rPos < tWidth:
            rightCnt +=1
            if trees[y][rPos] >= height: 
                break
            rPos+=1
        
        score = upCnt*downCnt*leftCnt*rightCnt
        senic[y][x] = score

        if score > maxScore: maxScore = score

print(maxScore)


