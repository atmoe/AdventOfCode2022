#!/usr/bin/python

import sys
import re
import copy

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

class Pos:                 
    def __init__(self, x, y):
        self.x = x   
        self.y = y
                     
    def __str__(self):   
        return f'({self.x},{self.y})'

jets = []
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    jets = list(line.rstrip())

board = [list('|' + '.' * 7 + '|'), list('|' + '.' * 7 + '|'), list('|' + '.' * 7 + '|'), list('+-------+')]

def getShapeLocs(s, root):
    locs = []
    if s == '-':
        locs.append(Pos(root.x,   root.y))
        locs.append(Pos(root.x+1, root.y))
        locs.append(Pos(root.x+2, root.y))
        locs.append(Pos(root.x+3, root.y))
    if s == '+':
        locs.append(Pos(root.x+1,  root.y))
        locs.append(Pos(root.x,    root.y+1))
        locs.append(Pos(root.x+1,  root.y+1))
        locs.append(Pos(root.x+2,  root.y+1))
        locs.append(Pos(root.x+1,  root.y+2))
    if s == 'l':
        locs.append(Pos(root.x+2,  root.y))
        locs.append(Pos(root.x+2,  root.y+1))
        locs.append(Pos(root.x+0,  root.y+2))
        locs.append(Pos(root.x+1,  root.y+2))
        locs.append(Pos(root.x+2,  root.y+2))
    if s == '|':
        locs.append(Pos(root.x,  root.y))
        locs.append(Pos(root.x,  root.y+1))
        locs.append(Pos(root.x,  root.y+2))
        locs.append(Pos(root.x,  root.y+3))
    if s == 'o':
        locs.append(Pos(root.x,   root.y))
        locs.append(Pos(root.x,   root.y+1))
        locs.append(Pos(root.x+1, root.y))
        locs.append(Pos(root.x+1, root.y+1))

    return locs

def printBoard(locs, b):
    printBoard = copy.deepcopy(b)
    for l in locs:
        printBoard[l.y][l.x] = '@'
    for b in printBoard:
        print("".join(b))


print("------------------")
print("---- PART 1 ------")
print("------------------")
shapes = ['-', '+', 'l', '|', 'o']
shapeH = [ 1,   3,   3,   4,   2]
shapePtr = 0
jetPtr = 0
tallestRow = 3

numShapes = 2022
for i in range(numShapes):
    s  = shapes[shapePtr]
    sH = shapeH[shapePtr]

    # grow board if needed
    while tallestRow - 3 - sH < 0:
        tallestRow += 1
        board.insert(0, list('|' + '.' * 7 + '|'))

    shapePos = Pos(3, tallestRow - 3 - sH)
    sLocs = getShapeLocs(s, shapePos)

    stopped = False
    while not stopped:
        ### blow gas ###
        if jets[jetPtr] == '>':
            delta = 1
        elif jets[jetPtr] == '<':
            delta = -1

        obstruction = False
        for l in sLocs:
            if board[l.y][l.x+delta] != '.':
                obstruction = True

        if not obstruction:
            for l in sLocs:
                l.x += delta
         
        ### drop ###
        obstruction = False
        for l in sLocs:
            if board[l.y+1][l.x] != '.':
                obstruction = True

        if obstruction:
            stopped = True
            for l in sLocs:
                if l.y < tallestRow:
                    tallestRow = l.y
                board[l.y][l.x] = '#'

        else:
            for l in sLocs:
                l.y += 1
         



        jetPtr = (jetPtr + 1) % len(jets)

    shapePtr = (shapePtr + 1) % 5

print(len(board) - tallestRow - 1)

print("------------------")
print("---- PART 2 ------")
print("------------------")



