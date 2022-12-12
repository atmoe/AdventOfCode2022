#!/usr/bin/python

import sys
import re
import math

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]

class Monkey:
    def __init__(self, num, items, op, testVal, t, f):
        self.num     = num
        self.items   = items
        self.op      = op
        self.test    = testVal
        self.tThrow  = t
        self.fThrow  = f
        self.inspections = 0

        self.itemsP2 = []
        for i in items:
            modHash = {}
            for p in primes:
                modHash[p] = i % p
            
            self.itemsP2.append(modHash)

    # return (throwMonkey, value)
    def testNextItem(self):
        self.inspections += 1
        level = self.items.pop(0)

        # Operation
        if self.op[2:] == 'old':
            if self.op[0] == '+': level = level + level
            if self.op[0] == '*': level = level * level
            if self.op[0] == '-': level = level - level
        else:
            if self.op[0] == '+': level = level + int(self.op[2:])
            if self.op[0] == '*': level = level * int(self.op[2:])
            if self.op[0] == '-': level = level - int(self.op[2:])

        
        level = int(math.floor(level/3))

        if level % self.test == 0:
            return (self.tThrow, level)
        else:
            return (self.fThrow, level)

    # return (throwMonkey, value)
    def testNextItemP2(self):
        self.inspections += 1
        item = self.itemsP2.pop(0)

        # Operation
        if self.op[2:] == 'old':
            for p in primes:
                item[p] = (item[p] * item[p]) % p

        else:
            if self.op[0] == '*':
                for p in primes:
                    item[p] = (item[p] * int(self.op[2:])) % p

            if self.op[0] == '+': 
                for p in primes:
                    item[p] = (item[p] + int(self.op[2:])) % p

        if item[self.test] == 0:
            return (self.tThrow, item)
        else:
            return (self.fThrow, item)

    def __str__(self):
        return f'{self.num}: {self.op} {self.test} t={self.tThrow} f={self.fThrow} {self.inspections}'
        


monkeys = []
inputFile = open(sys.argv[1], "r")

count  = 0
mNum   = -1
mItems = []
mOp    = ""
mTest  = -1
fThrow = -1
tThrow = -1
for line in inputFile.readlines():
    if count == 0:
        result = re.match('^Monkey (\d+):', line)
        mNum = result.group(1)
    elif count == 1:
        mItems = [int(x) for x in line.replace("  Starting items: ","").split(", ")]
    elif count == 2:
        result = re.match('^  Operation: new = old (.*)', line)
        mOp = result.group(1)
    elif count == 3:
        result = re.match('^  Test: divisible by (\d+)', line)
        mTest = int(result.group(1))
    elif count == 4:
        result = re.match('^    If true: throw to monkey (\d+)', line)
        tThrow = int(result.group(1))
    elif count == 5:
        result = re.match('^    If false: throw to monkey (\d+)', line)
        fThrow = int(result.group(1))
        monkey = Monkey(mNum, mItems, mOp, mTest, tThrow, fThrow)
        monkeys.append(monkey)
    elif count == 6:
        count = 0
        mNum   = -1
        mItems = []
        mOp    = ""
        mTest  = -1
        fThrow = -1
        tThrow = -1
        continue

    count += 1

for m in monkeys:
    print(m)


print("------------------")
print("---- PART 1 ------")
print("------------------")
doPart1 = False
if doPart1:
    for round in range(20):
        for m in monkeys:
            while len(m.items) > 0:
                throw = m.testNextItem()
                monkeys[throw[0]].items.append(throw[1])

    for m in monkeys:
        print(m)

    max0 = 0
    max1 = 0
    for m in monkeys:
        if m.inspections > max0:
            max1 = max0
            max0 = m.inspections
        elif m.inspections > max1:
            max1 = m.inspections

    print(max0*max1)


print("------------------")
print("---- PART 2 ------")
print("------------------")
for round in range(10000):
    for m in monkeys:
        while len(m.itemsP2) > 0:
            throw = m.testNextItemP2()
            monkeys[throw[0]].itemsP2.append(throw[1])

for m in monkeys:
    print(m)

max0 = 0
max1 = 0
for m in monkeys:
    if m.inspections > max0:
        max1 = max0
        max0 = m.inspections
    elif m.inspections > max1:
        max1 = m.inspections

print(max0*max1)





