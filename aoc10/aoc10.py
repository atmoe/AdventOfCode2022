#!/usr/bin/python

import sys
import re
import math

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

instrs = []
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    instr = line.rstrip().split()
    instrs.append(instr)

print("------------------")
print("---- PART 1 ------")
print("------------------")
total = 0
cycle = 0
regX = 1
for i in instrs:
    if i[0] == 'noop':
        cycle+=1 
    elif i[0] == 'addx':
        cycle+=1

    if cycle == 20:
        print(f'{cycle}: {regX} => {cycle*regX}')
        total += cycle*regX
    elif cycle > 20 and ((cycle-20) % 40 == 0):
        print(f'{cycle}: {regX} => {cycle*regX}')
        total += cycle*regX

    if i[0] == 'addx':
        cycle+=1

        if cycle == 20:
            print(f'{cycle}: {regX} => {cycle*regX}')
            total += cycle*regX
        elif cycle > 20 and ((cycle-20) % 40 == 0):
            print(f'{cycle}: {regX} => {cycle*regX}')
            total += cycle*regX

    if i[0] == 'addx':
        regX += int(i[1])

print(f'{total}')

print("------------------")
print("---- PART 2 ------")
print("------------------")
screen = [[], [], [], [], [], []]
for i in range(len(screen)):
    screen[i] = [' ' for x in range(40)]

cycle = 0
regX = 1
for i in instrs:
    xPos = cycle % 40
    if xPos >= regX-1 and xPos <= regX+1:
        screen[int(math.floor(cycle/40))][cycle%40] = '#'

    if i[0] == 'noop':
        cycle+=1
    elif i[0] == 'addx':
        cycle+=1


    if i[0] == 'addx':
        xPos = cycle % 40
        if xPos >= regX-1 and xPos <= regX+1:
            screen[int(math.floor(cycle/40))][cycle%40] = '#'

        cycle+=1


    if i[0] == 'addx':
        regX += int(i[1])

for s in screen:
    print("".join(s))




