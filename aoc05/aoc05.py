#!/usr/bin/python

import sys
import re
import copy

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

stacks = [[], [], [], [], [], [], [], [], [], []]
moves = []


getCrates = True
getMoves  = False 
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    if getCrates:
        line = line.rstrip()
        for i in range(0,len(line), 4):
            if line[i+1] == '1':
                getCrates = False 
                break

            if line[i+1] != ' ':
                stacks[int(i/4)].insert(0, line[i+1])


    elif not getMoves:
        getMoves = True
        continue

    elif getMoves:
        moveRe = re.match('^move (\d+) from (\d+) to (\d+)$', line)
        if not moveRe: 
            print('move not found')
            quit()
        moves.append((int(moveRe.group(1)), int(moveRe.group(2)), int(moveRe.group(3))))

for s in stacks:
    print(s)

for m in moves:
    print(m)

print("------------------")
print("---- PART 1 ------")
print("------------------")
stacksP1 = copy.deepcopy(stacks)

for m in moves:
    num = m[0]
    f = m[1]-1
    t = m[2]-1
    for i in range(num):
        stacksP1[t].append(stacksP1[f].pop())

for s in stacksP1:
    print(s)

result = ""
for s in stacksP1:
    if len(s) > 0:
        result += s[-1]

print(result)

print("------------------")
print("---- PART 2 ------")
print("------------------")
stacksP1 = copy.deepcopy(stacks)

for m in moves:
    num = m[0]
    f = m[1]-1
    t = m[2]-1

    popped = []
    for i in range(num):
        popped.append(stacksP1[f].pop())
    
    for i in range(num):
        stacksP1[t].append(popped.pop())

for s in stacksP1:
    print(s)

result = ""
for s in stacksP1:
    if len(s) > 0:
        result += s[-1]

print(result)


