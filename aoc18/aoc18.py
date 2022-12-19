#!/usr/bin/python

import sys
import re

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"
cubes   = []
cubeSet = set()
maxPos = [0, 0, 0]
minPos = [100000, 100000, 100000]
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    cube = [int(x) for x in line.rstrip().split(',')]
    cubeTuple = (cube[0], cube[1], cube[2])
    cubes.append(cubeTuple)
    cubeSet.add(tuple(cubeTuple))


    if cubeTuple[0] > maxPos[0]: maxPos[0] = cubeTuple[0]
    if cubeTuple[1] > maxPos[1]: maxPos[1] = cubeTuple[1]
    if cubeTuple[2] > maxPos[2]: maxPos[2] = cubeTuple[2]
    if cubeTuple[0] < minPos[0]: minPos[0] = cubeTuple[0]
    if cubeTuple[1] < minPos[1]: minPos[1] = cubeTuple[1]
    if cubeTuple[2] < minPos[2]: minPos[2] = cubeTuple[2]

print(minPos, maxPos)

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
freeEdges = 0
outerSet = set()
innerSet = set()
for c in cubes:
    #print('------------')
    #print('c = ', c)
    #print('o=', end='')
    #for o in outerSet:
    #    print(o, end='')
    #print()
    #print('i=', end='')
    #for i in innerSet:
    #    print(i, end='')
    #print()

    dirs = []
    dirs.append((c[0],   c[1]+1, c[2]))     # up
    dirs.append((c[0],   c[1]-1, c[2]))     # down
    dirs.append((c[0],   c[1],   c[2]+1))   # front
    dirs.append((c[0],   c[1],   c[2]-1))   # back
    dirs.append((c[0]+1, c[1],   c[2]))     # left
    dirs.append((c[0]-1, c[1],   c[2]))     # right

    for d in dirs:
        #print('-', d)
        if   d in cubeSet:
            #print('-- is cube')
            continue
        elif d in innerSet:
            #print('-- is inner')
            continue
        elif d in outerSet:
            #print('-- is outer')
            freeEdges+=1
            continue
        else:
            # unclassified neighbor
            #print('-- unclassified')
            potentialSet = set()
            potentialSet.add(d)
            nodesToClassify = [d]

            # trace until no neighbors added (inner) or x,y,z go past bounding box (outer)
            classified = False
            classification = None
            while len(nodesToClassify) > 0 and not classified:
                newNodes = []
                for n in nodesToClassify:
                    nDirs = []
                    nDirs.append((n[0],   n[1]+1, n[2]))     # up
                    nDirs.append((n[0],   n[1]-1, n[2]))     # down
                    nDirs.append((n[0],   n[1],   n[2]+1))   # front
                    nDirs.append((n[0],   n[1],   n[2]-1))   # back
                    nDirs.append((n[0]+1, n[1],   n[2]))     # left
                    nDirs.append((n[0]-1, n[1],   n[2]))     # right
                    for nd in nDirs:
                        #print('---', nd)
                        if   nd in cubeSet:
                            #print('----- cube')
                            continue
                        elif   nd in potentialSet:
                            #print('----- in set already')
                            continue
                        elif nd in innerSet:
                            print('should not be here!')
                            quit()
                        elif nd in outerSet:
                            #print('----- outer(found)')
                            potentialSet.add(nd) 
                            classified = True
                            classification = 'outer'
                            outerSet = outerSet.union(potentialSet)
                        elif nd[0] > maxPos[0] or nd[0] < minPos[0] or \
                             nd[1] > maxPos[1] or nd[1] < minPos[1] or \
                             nd[2] > maxPos[2] or nd[2] < minPos[2]:
                            #print('----- outer(range)')
                            potentialSet.add(nd) 
                            classified = True
                            classification = 'outer'
                            outerSet = outerSet.union(potentialSet)
                        else:
                            #print('----- unclassified')
                            potentialSet.add(nd) 
                            newNodes.append(nd)

                nodesToClassify = newNodes

            if not classified:
                innerSet = innerSet.union(potentialSet)
            if classification == 'outer':
                freeEdges+=1

print(freeEdges)





