#!/usr/bin/python

import sys
import re

assert len(sys.argv) == 2, sys.argv[0] + " requires 1 argument!"

class Node:
    def __init__(self, val, prev_ptr, next_ptr):
        self.val      = val
        self.prev_ptr = prev_ptr 
        self.next_ptr = next_ptr


head = None
prevNode = None
ptrArr = []

inputFile = open(sys.argv[1], "r")
for line in inputFile.readlines():
    val = int(line.rstrip())

    n = Node(val, prevNode, None)

    if prevNode:
        prevNode.next_ptr = n
    else:
        head = n

    ptrArr.append(n)
    prevNode = n
inputFile.close()

prevNode.next_ptr = head
head.prev_ptr = prevNode


print("------------------")
print("---- PART 1 ------")
print("------------------")
#printPtr = head
#for i in range(len(ptrArr)):
#    print(printPtr.val, ', ', end='')
#    printPtr = printPtr.next_ptr
#print()
#printPtr = head
#for i in range(len(ptrArr)):
#    print(printPtr.val, ', ', end='')
#    printPtr = printPtr.prev_ptr
#print()



for p in ptrArr:
    #print(f"--- moving {p.val} ---")
    if p.val == 0: continue

    # remove from list
    p.prev_ptr.next_ptr = p.next_ptr
    p.next_ptr.prev_ptr = p.prev_ptr

    if p.val > 0:
        insertPtr = p.next_ptr
        for i in range(p.val-1):
            insertPtr = insertPtr.next_ptr

        #print(f'inserting after {insertPtr.val}')
        p.next_ptr = insertPtr.next_ptr
        p.prev_ptr = insertPtr

        insertPtr.next_ptr.prev_ptr = p
        insertPtr.next_ptr = p

    elif p.val < 0:
        insertPtr = p.prev_ptr
        for i in range(abs(p.val)-1):
            insertPtr = insertPtr.prev_ptr

        #print(f'inserting before {insertPtr.val}')
        p.next_ptr = insertPtr
        p.prev_ptr = insertPtr.prev_ptr

        insertPtr.prev_ptr.next_ptr = p
        insertPtr.prev_ptr = p

    #printPtr = head
    #for i in range(len(ptrArr)):
    #    print(printPtr.val, ', ', end='')
    #    printPtr = printPtr.next_ptr
    #print()
    #printPtr = head
    #for i in range(len(ptrArr)):
    #    print(printPtr.val, ', ', end='')
    #    printPtr = printPtr.prev_ptr
    #print()

# find zero
ptr = head
while ptr.val != 0:
    ptr = ptr.next_ptr

count = 0
val1k = 0
val2k = 0
val3k = 0
for i in range(3000):
    ptr = ptr.next_ptr
    if i ==  999: val1k = ptr.val
    if i == 1999: val2k = ptr.val
    if i == 2999: val3k = ptr.val

print(val1k + val2k + val3k)
        
quit()
print("------------------")
print("---- PART 2 ------")
print("------------------")
