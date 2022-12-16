#!/usr/bin/python

import sys
import re

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

pairs = []
inputFile = open(sys.argv[1], "r")
count = 0
pair = []
for line in inputFile.readlines():
    if count < 2:
        pair.append(line.rstrip())
        if count == 1:
            pairs.append(pair)

        count += 1
    elif count == 2:
        pair = []
        count = 0


def getList(lStr):
    l = None
    listStk = []
    for i in range(len(lStr)):
        #print(l)
        # if [ update create new list, and update pointer stack
        r = re.match('^\[', lStr[i:])
        if r:
            newList = []
            if l == None:
                l = []
                listStk.append(l)
            else:
                listStk[-1].append(newList)
                listStk.append(newList)
        
        # if ] pop list pointer stack
        r = re.match('^\]', lStr[i:])
        if r:
            listStk.pop()

        # if number push to current list
        r = re.match('^(\d+)', lStr[i:])
        if r:
            if lStr[i-1].isnumeric(): continue

            listStk[-1].append(int(r.group(1)))

    return l

lPairs = []
for p in pairs:
    left  = getList(p[0])
    right = getList(p[1])
    lPairs.append([left, right])

def compare(l, r):
    #print(f'compare {l} vs {r}')

    if type(l) == int:
        if l == r: return 'continue'
        if r <  l: return 'out of order'
        if r >  l: return 'in order'

    if not type(l) == list or not type(r) == list:
        print('not lists!')
        quit()
    
    for i in range(len(l)):
        if i == len(r):
            return 'out of order'

        if type(l[i]) == int:
            if type(r[i]) == int:
                # both ints
                lTerm = l[i]
                rTerm = r[i]
            else:
                # only left int
                lTerm = [l[i]]
                rTerm = r[i]
        elif type(l[i]) == list:
            if type(r[i]) == int:
                # only right int
                lTerm = l[i]
                rTerm = [r[i]]
            else:
                # both lists
                lTerm = l[i]
                rTerm = r[i]

        rval = compare(lTerm, rTerm)
        if rval != 'continue':
            return rval

    if len(l) < len(r):
        return 'in order'
    else:
        return 'continue'

print("------------------")
print("---- PART 1 ------")
print("------------------")

idx = 1
count = 0
for p in lPairs:
    order = compare(p[0], p[1])
    if order == 'in order':
        count += idx
        
    idx += 1

print(count)

print("------------------")
print("---- PART 2 ------")
print("------------------")

sortedList = []
for p in lPairs:
    sortedList.append(p[0])
    sortedList.append(p[1])
sortedList.append([[2]])
sortedList.append([[6]])


for i in range(len(sortedList)-1):
    for j in range(len(sortedList) - i - 1):
        if compare(sortedList[j], sortedList[j+1]) == 'out of order':
            tmp = sortedList[j]
            sortedList[j] = sortedList[j+1]
            sortedList[j+1] = tmp

idx = 1
mult = 1
for p in sortedList:
    if p == [[2]] or p == [[6]]:
        mult *= idx
    idx+=1

print(mult)


