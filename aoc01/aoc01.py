#!/usr/bin/python

import sys
import re

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

print("------------------")
print("---- PART 1 ------")
print("------------------")
maxCals = 0
iCals = 0

inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    line = line.rstrip()
    if line == "":
        if iCals > maxCals:
            maxCals = iCals

        iCals = 0
    else:
        iCals += int(line)

inputFile.close()

print(maxCals)



print("------------------")
print("---- PART 2 ------")
print("------------------")


cals = []
iCals=0
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    line = line.rstrip()
    if line == "":
        cals.append(iCals)
        iCals = 0
    else:
        iCals += int(line)

inputFile.close()
cals.sort()

print(cals[-1]+cals[-2]+cals[-3])


