#!/usr/bin/python

import sys
import re

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

sacks = []
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    sacks.append(line.rstrip())
    
print("------------------")
print("---- PART 1 ------")
print("------------------")

score = 0
for s in sacks:
    f = s[0:int(len(s)/2)]
    s = s[int(len(s)/2):]
    for i in f:
        if i in s:
            if i.isupper():
                score += (ord(i) - ord('A')+27)
            else:
                score+= (ord(i) - ord('a')+1)
            break

print(score)


print("------------------")
print("---- PART 2 ------")
print("------------------")
score=0
for i in range(int(len(sacks)/3)):
    sack0 = sacks[i*3]
    sack1 = sacks[i*3+1]
    sack2 = sacks[i*3+2]
    for s in sack0:
        if s in sack1 and s in sack2:
            if s.isupper():
                score += (ord(s) - ord('A')+27)
            else:
                score+= (ord(s) - ord('a')+1)
            break

print(score)




