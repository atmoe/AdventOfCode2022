#!/usr/bin/python

import sys
import re

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

pairs = []
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    lineRe = re.match('^(\d+)-(\d+),(\d+)-(\d+)', line)
    first  = (int(lineRe.group(1)), int(lineRe.group(2)))
    second = (int(lineRe.group(3)), int(lineRe.group(4)))
    pairs.append([first, second])

for p in pairs:
    print(p)

print("------------------")
print("---- PART 1 ------")
print("------------------")
contains = 0
for p in pairs:
    if (p[0][0] <= p [1][0] and p[0][1] >= p [1][1]) or \
       (p[1][0] <= p [0][0] and p[1][1] >= p [0][1]):
        contains += 1

print(contains)



print("------------------")
print("---- PART 2 ------")
print("------------------")
overlap = 0
for p in pairs:
    if (p[0][0] >= p [1][0] and p[0][0] <= p [1][1]) or \
       (p[0][1] >= p [1][0] and p[0][1] <= p [1][1]) or \
       (p[0][0] <= p [1][0] and p[0][1] >= p [1][1]) or \
       (p[1][0] <= p [0][0] and p[1][1] >= p [0][1]):

        overlap += 1

print(overlap)





