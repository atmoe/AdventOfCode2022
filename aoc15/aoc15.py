#!/usr/bin/python

import sys
import re

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x},{self.y})'
    

class Sensor:
    def __init__(self, sX, sY, bX, bY):
        self.pos = Pos(sX, sY)
        self.bPos = Pos(bX, bY)
        self.dist = abs(sX-bX) + abs(sY-bY)

    def __str__(self):
        return f'{self.pos} {self.dist} -> {self.bPos}'

sensors = []
beacons = []
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    line = line.rstrip()
    sre = re.match('^Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)$', line)
    if not sre:
        print('no match')
        quit()

    sensors.append(Sensor(int(sre.group(1)), int(sre.group(2)), int(sre.group(3)), int(sre.group(4))))
    
    beacon = Pos(int(sre.group(3)), int(sre.group(4)))
    found = False
    for b in beacons:
        if beacon.x == b.x and beacon.y == b.y:
            found = True
            break

    if not found:
        beacons.append(beacon)

for s in sensors:
    print(s)
for b in beacons:
    print(b)

print("------------------")
print("---- PART 1 ------")
print("------------------")
targ = 10
hitRanges = []
for s in sensors:
    distAlongTarg = 0
    if s.pos.y <= targ and s.pos.y + s.dist >= targ:
        distAlongTarg = (s.dist) - (targ - s.pos.y - 1)

    if s.pos.y >= targ and s.pos.y - s.dist <= targ:
        distAlongTarg = (s.dist) - (s.pos.y - targ - 1)

    if distAlongTarg == 0: continue

    minRange = s.pos.x - (distAlongTarg - 1)
    maxRange = s.pos.x + (distAlongTarg - 1)
    r = [minRange, maxRange]

    hitRanges.append(r)
    lastLen = 0
    intersected = False
    while lastLen != len(hitRanges):
        lastLen = len(hitRanges)

        newHitRanges = []

        for h_insert in hitRanges:
            intersected = False
            for idx,h_exist in enumerate(newHitRanges):
                #  hhhhhhhhhhhhhhhhhhhhh
                #       rrrrrrrrrrr     
                if h_insert[0] >= h_exist[0] and h_insert[1] <= h_exist[1]:
                    # fully within existing range
                    intersected = True
                    break

                #     hhhhh
                #  rrrrrrrrrrr     
                if h_insert[0] <= h_exist[0] and h_insert[1] >= h_exist[1]:
                    # fully covers existing range
                    newHitRanges[idx][0] = h_insert[0]
                    newHitRanges[idx][1] = h_insert[1]
                    intersected = True
                    break

                #     hhhhhhhhhhhh
                #  rrrrrrrrrrr     
                if h_insert[0] < h_exist[0] and h_insert[1] >= h_exist[0] and h_insert[1] <= h_exist[1]:
                    newHitRanges[idx][0] = h_insert[0]
                    newHitRanges[idx][1] = h_exist[1]
                    intersected = True
                    break


                #  hhhhhhhhhhhh
                #       rrrrrrrrrrr     
                if h_insert[0] >= h_exist[0] and h_insert[0] <= h_exist[1] and h_insert[1]> h_exist[1]:
                    newHitRanges[idx][0] = h_exist[0]
                    newHitRanges[idx][1] = h_insert[1]
                    intersected = True
                    break

            if not intersected:
                newHitRanges.append(h_insert)

            hitRanges = newHitRanges

count = 0
for r in hitRanges:
    count += (r[1] - r[0] + 1)
    for b in beacons:
        if b.y == targ and r[0] <= b.x and r[1] >= b.x:
            count-=1

print(count)

print("------------------")
print("---- PART 2 ------")
print("------------------")
targ = 4000000
for y in range(targ):
    hitRanges = []
    for s in sensors:
        distAlongTarg = 0
        if s.pos.y <= y and s.pos.y + s.dist >= y:
            distAlongTarg = (s.dist) - (y- s.pos.y - 1)
    
        if s.pos.y >= y and s.pos.y - s.dist <= y:
            distAlongTarg = (s.dist) - (s.pos.y - y - 1)
    
        if distAlongTarg == 0: continue
    
        minRange = s.pos.x - (distAlongTarg - 1)
        maxRange = s.pos.x + (distAlongTarg - 1)
        r = [minRange, maxRange]
    
        hitRanges.append(r)
        lastLen = 0
        intersected = False
        while lastLen != len(hitRanges):
            lastLen = len(hitRanges)
    
            newHitRanges = []
    
            for h_insert in hitRanges:
                intersected = False
                for idx,h_exist in enumerate(newHitRanges):
                    #  hhhhhhhhhhhhhhhhhhhhh
                    #       rrrrrrrrrrr     
                    if h_insert[0] >= h_exist[0] and h_insert[1] <= h_exist[1]:
                        # fully within existing range
                        intersected = True
                        break
    
                    #     hhhhh
                    #  rrrrrrrrrrr     
                    if h_insert[0] <= h_exist[0] and h_insert[1] >= h_exist[1]:
                        # fully covers existing range
                        newHitRanges[idx][0] = h_insert[0]
                        newHitRanges[idx][1] = h_insert[1]
                        intersected = True
                        break
    
                    #     hhhhhhhhhhhh
                    #  rrrrrrrrrrr     
                    if h_insert[0] < h_exist[0] and h_insert[1] >= h_exist[0] and h_insert[1] <= h_exist[1]:
                        newHitRanges[idx][0] = h_insert[0]
                        newHitRanges[idx][1] = h_exist[1]
                        intersected = True
                        break
    
    
                    #  hhhhhhhhhhhh
                    #       rrrrrrrrrrr     
                    if h_insert[0] >= h_exist[0] and h_insert[0] <= h_exist[1] and h_insert[1]> h_exist[1]:
                        newHitRanges[idx][0] = h_exist[0]
                        newHitRanges[idx][1] = h_insert[1]
                        intersected = True
                        break
    
                if not intersected:
                    newHitRanges.append(h_insert)
    
                hitRanges = newHitRanges
    
    
    
    count = 0
    possibleX = -1
    for r in hitRanges:
        if r[0] < 0:
            lower = 0
        elif r[0] >= targ:
            lower = targ
        else:
            lower = r[0]

        if r[1] < 0:
            upper = 0
        elif r[1] >= targ:
            upper = targ
        else:
            upper = r[1]

        if upper >= 0 and possibleX == -1:
            possibleX = upper+1

        count += (upper - lower + 1)
    
    if count != targ + 1:
        print(y, count)
        print(possibleX*4000000+y)
        break
    




