#!/usr/bin/python

import sys
import re

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

moves = []
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    m = line.split()
    moves.append([m[0], int(m[1])])


class Pos:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x}_{self.y}'


print("------------------")
print("---- PART 1 ------")
print("------------------")
visited = {}
hPos = Pos(0,0)
tPos = Pos(0,0)

visited[str(tPos)] = True

for m in moves:
    for i in range(m[1]):
        # Move Head
        if   m[0] == 'R': hPos = Pos(hPos.x+1, hPos.y)
        elif m[0] == 'L': hPos = Pos(hPos.x-1, hPos.y)
        elif m[0] == 'U': hPos = Pos(hPos.x, hPos.y+1)
        elif m[0] == 'D': hPos = Pos(hPos.x, hPos.y-1)

        # Move tail
        deltaX = hPos.x - tPos.x
        deltaY = hPos.y - tPos.y

        touching = abs(deltaX) < 2 and abs(deltaY) < 2

        if not touching:
            if   deltaY == 0 and deltaX > 0:  tPos = Pos(tPos.x+1, tPos.y)
            elif deltaY == 0 and deltaX < 0:  tPos = Pos(tPos.x-1, tPos.y)
            elif deltaX == 0 and deltaY > 0:  tPos = Pos(tPos.x, tPos.y+1)
            elif deltaX == 0 and deltaY < 0:  tPos = Pos(tPos.x, tPos.y-1)
            elif deltaX > 0 and deltaY > 0:   tPos = Pos(tPos.x+1, tPos.y+1)
            elif deltaX > 0 and deltaY < 0:   tPos = Pos(tPos.x+1, tPos.y-1)
            elif deltaX < 0 and deltaY > 0:   tPos = Pos(tPos.x-1, tPos.y+1)
            elif deltaX < 0 and deltaY < 0:   tPos = Pos(tPos.x-1, tPos.y-1)

        visited[str(tPos)] = True

print(len(visited))




print("------------------")
print("---- PART 2 ------")
print("------------------")
tVisited = {}

positions = [Pos(0,0),
             Pos(0,0),
             Pos(0,0),
             Pos(0,0),
             Pos(0,0),
             Pos(0,0),
             Pos(0,0),
             Pos(0,0),
             Pos(0,0),
             Pos(0,0)]

tVisited[str(positions[-1])] = True

for m in moves:
    for i in range(m[1]):
        # Move Head
        if   m[0] == 'R': positions[0] = Pos(positions[0].x+1, positions[0].y)
        elif m[0] == 'L': positions[0] = Pos(positions[0].x-1, positions[0].y)
        elif m[0] == 'U': positions[0] = Pos(positions[0].x,   positions[0].y+1)
        elif m[0] == 'D': positions[0] = Pos(positions[0].x,   positions[0].y-1)

        # Move remainder
        for i in range(1,len(positions)):
            lPos = positions[i-1]  # leading position
            tPos = positions[i]  # this position
            deltaX = lPos.x - tPos.x
            deltaY = lPos.y - tPos.y

            touching = abs(deltaX) < 2 and abs(deltaY) < 2

            if not touching:
                if   deltaY == 0 and deltaX > 0:  positions[i] = Pos(tPos.x+1, tPos.y)
                elif deltaY == 0 and deltaX < 0:  positions[i] = Pos(tPos.x-1, tPos.y)
                elif deltaX == 0 and deltaY > 0:  positions[i] = Pos(tPos.x, tPos.y+1)
                elif deltaX == 0 and deltaY < 0:  positions[i] = Pos(tPos.x, tPos.y-1)
                elif deltaX > 0 and deltaY > 0:   positions[i] = Pos(tPos.x+1, tPos.y+1)
                elif deltaX > 0 and deltaY < 0:   positions[i] = Pos(tPos.x+1, tPos.y-1)
                elif deltaX < 0 and deltaY > 0:   positions[i] = Pos(tPos.x-1, tPos.y+1)
                elif deltaX < 0 and deltaY < 0:   positions[i] = Pos(tPos.x-1, tPos.y-1)


        tVisited[str(positions[-1])] = True

print(len(tVisited))





