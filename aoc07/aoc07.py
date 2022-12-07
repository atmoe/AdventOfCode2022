#!/usr/bin/python

import sys
import re

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.size = 0
        self.total = 0
        self.subdirs = {}

fsys = Dir('/', None)
dirPtrs = [fsys]

fptr = fsys

commandLS = False
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    line = line.rstrip()

    cdRe  = re.match('\$ cd (.*)', line)
    lsRe  = re.match('\$ ls', line)
    dirRe = re.match('dir (.*)', line)
    fileRe = re.match('(\d+) (.*)', line)

    if cdRe:
        chngDir = cdRe.group(1)
        if chngDir == '/': continue

        elif chngDir == '..':
            fptr = fptr.parent
        else:
            fptr = fptr.subdirs[chngDir]

    elif lsRe:
        continue
    elif dirRe:
        name = dirRe.group(1)

        if name not in fptr.subdirs:
            newDir = Dir(name, fptr)
            fptr.subdirs[name] = newDir

            dirPtrs.append(newDir)

        continue
    elif fileRe:
        fptr.size += int(fileRe.group(1))
        
        pPtr= fptr.parent
        while pPtr != None:
            pPtr.size += int(fileRe.group(1))
            pPtr = pPtr.parent

inputFile.close()

print("------------------")
print("---- PART 1 ------")
print("------------------")

sumSize = 0
for d in dirPtrs:
    if d.size <= 100000:
        sumSize+=d.size

print(sumSize)

print("------------------")
print("---- PART 2 ------")
print("------------------")
unusedSpace = 70000000 - fsys.size
requiredToFree = 30000000 - unusedSpace
minDirSize = 70000000
for d in dirPtrs:
    if d.size >= requiredToFree and d.size < minDirSize:
        minDirSize = d.size

print(minDirSize)



