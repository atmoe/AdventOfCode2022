#!/usr/bin/python

import sys
import re
import copy

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

monkeysFound = {}
monkeysOperations = []
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    numRe  = re.match('^(....): (\d+)$', line)
    mathRe = re.match('^(....): (....) (.) (....)$', line)
    if numRe:
        monkeysFound[numRe.group(1)] = int(numRe.group(2))
    if mathRe:
        name = mathRe.group(1)
        op1  = mathRe.group(2)
        op2  = mathRe.group(4)
        op   = mathRe.group(3)
        monkeysOperations.append([name, op1, op2, op])

print(monkeysOperations)

print("------------------")
print("---- PART 1 ------")
print("------------------")
p1Operations = copy.deepcopy(monkeysOperations)
p1Found      = copy.deepcopy(monkeysFound)
while len(p1Operations) > 0:
    p1OperationsNext = []
    for o in p1Operations:
        if o[1] in p1Found and o[2] in p1Found:
            if o[3] == '+': p1Found[o[0]] = p1Found[o[1]] + p1Found[o[2]]
            if o[3] == '-': p1Found[o[0]] = p1Found[o[1]] - p1Found[o[2]]
            if o[3] == '*': p1Found[o[0]] = p1Found[o[1]] * p1Found[o[2]]
            if o[3] == '/': p1Found[o[0]] = int(p1Found[o[1]] / p1Found[o[2]])
        else:
            p1OperationsNext.append(o)

        p1Operations = p1OperationsNext

print(p1Found['root'])

print("------------------")
print("---- PART 2 ------")
print("------------------")
p2Operations = copy.deepcopy(monkeysOperations)
p2Found      = copy.deepcopy(monkeysFound)

for o in p2Operations:
    if o[0] == 'root':
        o[3] = '='
        break

testVal = 1
testValAdj = 10000000000
deltaPos = True
equal = False
while not equal:
    print(testVal, "    ", end='')
    ops   = copy.deepcopy(p2Operations)
    found = copy.deepcopy(p2Found)

    found['humn'] = testVal

    while len(ops) > 0:
        opsNext = []
        for o in ops:
            if o[1] in found and o[2] in found:
                if o[3] == '+': found[o[0]] = found[o[1]] + found[o[2]]
                if o[3] == '-': found[o[0]] = found[o[1]] - found[o[2]]
                if o[3] == '*': found[o[0]] = found[o[1]] * found[o[2]]
                if o[3] == '/': found[o[0]] = int(found[o[1]] / found[o[2]])
                if o[3] == '=':
                    found[o[0]] = found[o[1]] == found[o[2]]

                    if found[o[1]] < found[o[2]] and deltaPos:
                        testValAdj = -1
                        deltaPos = False
                    elif found[o[1]] < found[o[2]]:
                        testValAdj *= 2

                    if found[o[1]] > found[o[2]] and not deltaPos:
                        testValAdj = 1
                        deltaPos = True
                    elif found[o[1]] > found[o[2]]:
                        testValAdj *= 2


                    print(found[o[1]], found[o[2]], found[o[1]] - found[o[2]])
            else:
                opsNext.append(o)

        ops = opsNext 
    
    
    if found['root']:
        equal = True
    else:
        testVal+=testValAdj


print(testVal)



