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

for p in pairs:
    print(p[0], "vs", p[1])


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
    print("========================")
    left  = getList(p[0])
    right = getList(p[1])
    lPairs.append([left, right])

def compare(l, r):
    print(f'compare {l} vs {r}')

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
    print('--------------------------')
    order = compare(p[0], p[1])
    if order == 'in order':
        count += idx
        
    print(f'Final = {order}')

    idx += 1

print(count)

quit()
print("------------------")
print("---- PART 2 ------")
print("------------------")




