#!/usr/bin/python

import sys
import re

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    signal = line
inputFile.close()

print("------------------")
print("---- PART 1 ------")
print("------------------")
for idx, s in enumerate(signal):
    substr = signal[idx:idx+4]
    unique = {}
    for s in substr:
        unique[s] = 1

    if len(unique) == 4:
        print(idx+4)
        break

print("------------------")
print("---- PART 2 ------")
print("------------------")
for idx, s in enumerate(signal):
    substr = signal[idx:idx+14]
    unique = {}
    for s in substr:
        unique[s] = 1

    if len(unique) == 14:
        print(idx+14)
        break
 


