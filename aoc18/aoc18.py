#!/usr/bin/python

import sys
import re

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"
cubes   = []
cubeSet = set()

inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    cube = [int(x) for x in line.rstrip().split(',')]
    cubeTuple = (cube[0], cube[1], cube[2])
    cubes.append(cubeTuple)
    cubeSet.add(tuple(cubeTuple))


print("------------------")
print("---- PART 1 ------")
print("------------------")
freeEdges = 0
for c in cubes:
    up    = (c[0],   c[1]+1, c[2])
    down  = (c[0],   c[1]-1, c[2])
    front = (c[0],   c[1],   c[2]+1)
    back  = (c[0],   c[1],   c[2]-1)
    left  = (c[0]+1, c[1],   c[2])
    right = (c[0]-1, c[1],   c[2])

    if up    not in cubeSet: freeEdges+=1
    if down  not in cubeSet: freeEdges+=1
    if front not in cubeSet: freeEdges+=1
    if back  not in cubeSet: freeEdges+=1
    if left  not in cubeSet: freeEdges+=1
    if right not in cubeSet: freeEdges+=1

print(freeEdges)

print("------------------")
print("---- PART 2 ------")
print("------------------")




