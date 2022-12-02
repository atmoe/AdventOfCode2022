#!/usr/bin/python

import sys
import re

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"


print("------------------")
print("---- PART 1 ------")
print("------------------")

score = 0
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    pair = line.rstrip().split()

    # AX - Rock
    # BY - Paper
    # CZ - Scissors

    if pair[0] == "A" and pair[1] == "X":
        score += 1
        score += 3
    if pair[0] == "A" and pair[1] == "Y":
        score += 2
        score += 6
    if pair[0] == "A" and pair[1] == "Z":
        score += 3
        score += 0

    if pair[0] == "B" and pair[1] == "X":
        score += 1
        score += 0
    if pair[0] == "B" and pair[1] == "Y":
        score += 2
        score += 3
    if pair[0] == "B" and pair[1] == "Z":
        score += 3
        score += 6

    if pair[0] == "C" and pair[1] == "X":
        score += 1
        score += 6
    if pair[0] == "C" and pair[1] == "Y":
        score += 2
        score += 0
    if pair[0] == "C" and pair[1] == "Z":
        score += 3
        score += 3

inputFile.close()


print(score)


print("------------------")
print("---- PART 2 ------")
print("------------------")

score = 0
inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    pair = line.rstrip().split()

    # AX - Rock
    # BY - Paper
    # CZ - Scissors

    if pair[0] == "A" and pair[1] == "X":  # Lose
        score += 3
        score += 0
    if pair[0] == "A" and pair[1] == "Y":  # Draw
        score += 1
        score += 3
    if pair[0] == "A" and pair[1] == "Z":  # Win
        score += 2
        score += 6

    if pair[0] == "B" and pair[1] == "X":
        score += 1
        score += 0
    if pair[0] == "B" and pair[1] == "Y":
        score += 2
        score += 3
    if pair[0] == "B" and pair[1] == "Z":
        score += 3
        score += 6

    if pair[0] == "C" and pair[1] == "X":
        score += 2
        score += 0
    if pair[0] == "C" and pair[1] == "Y":
        score += 3
        score += 3
    if pair[0] == "C" and pair[1] == "Z":
        score += 1
        score += 6

print(score)


