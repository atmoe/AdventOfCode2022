#!/usr/bin/python

import sys
import re
import copy

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

heightMap = []
distMap   = []
visitMap  = []
sPos = (0,0)
ePos = (0,0)
y = 0
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    row = list(line.rstrip())

    heightMap.append(row)
    distMap.append([1000000000000 for x in range(len(row))])
    visitMap.append([False for x in range(len(row))])
    
    x = 0
    for r in row:
        if r == 'S':
            sPos = (x, y)
            distMap[y][x] = 0

        if r == 'E':
            ePos = (x, y)

        x+=1

    y+=1

mW = len(heightMap[0])
mH = len(heightMap)
print('-------------------')
#for row in heightMap:
#    print(row)
print('-------------------')
#for row in distMap:
#    print(row)
print('-------------------')
#for row in visitMap:
#    print(row)
print(f's = {sPos}')
print(f'e = {ePos}')


print("------------------")
print("---- PART 1 ------")
print("------------------")
p1DistMap  = copy.deepcopy(distMap)
p1VisitMap = copy.deepcopy(visitMap)

curPos = sPos
while curPos != ePos:
    cx = curPos[0]
    cy = curPos[1]

    #print("-----------------")
    #print(curPos)
    #print(f'd = {distMap[cy][cx]}')

    #for row in visitMap:
    #    for v in row:
    #        if v:
    #            print('x', end='')
    #        else:
    #            print('.', end='')
    #    print('')

    newDist = p1DistMap[cy][cx] + 1
    curLet = heightMap[cy][cx]

    # update distances to neighbors
    dirs = []
    if cx - 1 >= 0: # left
        if heightMap[cy][cx-1] == 'E':
            checkLet = 'z'
        else:
            checkLet = heightMap[cy][cx-1]

        delta = ord(checkLet) - ord(curLet)
        if delta <= 1 or heightMap[cy][cx] == 'S':
            #print(f'   lf -> d={delta} n={heightMap[cy][cx-1]} cur={curLet}')
            dirs.append((cx-1, cy))

    if cx + 1 < mW: # right
        if heightMap[cy][cx+1] == 'E':
            checkLet = 'z'
        else:
            checkLet = heightMap[cy][cx+1]

        delta = ord(checkLet) - ord(curLet)
        if delta <= 1 or heightMap[cy][cx] == 'S':
            #print(f'   rt -> d={delta} n={heightMap[cy][cx+1]} cur={curLet}')
            dirs.append((cx+1, cy))

    if cy - 1 >= 0: # up
        if heightMap[cy-1][cx] == 'E':
            checkLet = 'z'
        else:
            checkLet = heightMap[cy-1][cx]

        delta = ord(checkLet) - ord(curLet)
        if delta <= 1 or heightMap[cy][cx] == 'S':
            #print(f'   up -> d={delta} n={heightMap[cy-1][cx]} cur={curLet}')
            dirs.append((cx, cy-1))

    if cy + 1 < mH: # down
        if heightMap[cy+1][cx] == 'E':
            checkLet = 'z'
        else:
            checkLet = heightMap[cy+1][cx]

        delta = ord(checkLet) - ord(curLet)
        if delta <= 1 or heightMap[cy][cx] == 'S':
            #print(f'   dn -> d={delta} n={heightMap[cy+1][cx]} cur={curLet}')
            dirs.append((cx, cy+1))

    for d in dirs:
        dx = d[0]
        dy = d[1]
        if not p1VisitMap[dy][dx]:
            if p1DistMap[dy][dx] > newDist:
                p1DistMap[dy][dx] = newDist

    # mark node as visited
    p1VisitMap[cy][cx] = True

    # get next node
    nextDist = 10000000000000000
    nextPos = (0,0)
    for y in range(mH):
        for x in range(mW):
            if not p1VisitMap[y][x] and p1DistMap[y][x] < nextDist:
                nextDist = p1DistMap[y][x]
                nextPos = (x, y)
    curPos = nextPos

print(p1DistMap[curPos[1]][curPos[0]])


print("------------------")
print("---- PART 2 ------")
print("------------------")
lowestTotal = 100000000000000
for curY in range(mH):
    for curX in range(mW):
        if heightMap[curY][curX] not in ['S', 'a']: continue


        #print("NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN")

        p2DistMap  = copy.deepcopy(distMap)
        p2DistMap[sPos[1]][sPos[0]] = 1000000000000
        p2DistMap[curY][curX] = 0

        p2VisitMap = copy.deepcopy(visitMap)



        curPos = (curX, curY)
        while curPos != ePos:
            cx = curPos[0]
            cy = curPos[1]

            #print("-----------------")
            #print(curPos)
            #print(f'd = {distMap[cy][cx]}')
        
            #for row in p2VisitMap:
            #    for v in row:
            #        if v:
            #            print('x', end='')
            #        else:
            #            print('.', end='')
            #    print('')
        
            newDist = p2DistMap[cy][cx] + 1
            curLet = heightMap[cy][cx]
        
            # update distances to neighbors
            dirs = []
            if cx - 1 >= 0: # left
                if heightMap[cy][cx-1] == 'E':
                    checkLet = 'z'
                elif heightMap[cy][cx-1] == 'S':
                    checkLet = 'a'
                else:
                    checkLet = heightMap[cy][cx-1]
        
                delta = ord(checkLet) - ord(curLet)
                if delta <= 1 or heightMap[cy][cx] == 'S':
                    #print(f'   lf -> d={delta} n={heightMap[cy][cx-1]} cur={curLet}')
                    dirs.append((cx-1, cy))
        
            if cx + 1 < mW: # right
                if heightMap[cy][cx+1] == 'E':
                    checkLet = 'z'
                elif heightMap[cy][cx+1] == 'S':
                    checkLet = 'a'
                else:
                    checkLet = heightMap[cy][cx+1]
        
                delta = ord(checkLet) - ord(curLet)
                if delta <= 1 or heightMap[cy][cx] == 'S':
                    #print(f'   rt -> d={delta} n={heightMap[cy][cx+1]} cur={curLet}')
                    dirs.append((cx+1, cy))
        
            if cy - 1 >= 0: # up
                if heightMap[cy-1][cx] == 'E':
                    checkLet = 'z'
                elif heightMap[cy-1][cx] == 'S':
                    checkLet = 'a'
                else:
                    checkLet = heightMap[cy-1][cx]
        
                delta = ord(checkLet) - ord(curLet)
                if delta <= 1 or heightMap[cy][cx] == 'S':
                    #print(f'   up -> d={delta} n={heightMap[cy-1][cx]} cur={curLet}')
                    dirs.append((cx, cy-1))
        
            if cy + 1 < mH: # down
                if heightMap[cy+1][cx] == 'E':
                    checkLet = 'z'
                elif heightMap[cy+1][cx] == 'S':
                    checkLet = 'a'
                else:
                    checkLet = heightMap[cy+1][cx]
        
                delta = ord(checkLet) - ord(curLet)
                if delta <= 1 or heightMap[cy][cx] == 'S':
                    #print(f'   dn -> d={delta} n={heightMap[cy+1][cx]} cur={curLet}')
                    dirs.append((cx, cy+1))
        
            for d in dirs:
                dx = d[0]
                dy = d[1]
                if not p2VisitMap[dy][dx]:
                    if p2DistMap[dy][dx] > newDist:
                        p2DistMap[dy][dx] = newDist
        
            # mark node as visited
            p2VisitMap[cy][cx] = True
        
            # get next node
            nextDist = 10000000000000000
            nextPos = (0,0)
            for y in range(mH):
                for x in range(mW):
                    if not p2VisitMap[y][x] and p2DistMap[y][x] < nextDist:
                        nextDist = p2DistMap[y][x]
                        nextPos = (x, y)
            curPos = nextPos
        
        print(p2DistMap[curPos[1]][curPos[0]])
        if p2DistMap[curPos[1]][curPos[0]] < lowestTotal:
            lowestTotal = p2DistMap[curPos[1]][curPos[0]]

print(lowestTotal)



