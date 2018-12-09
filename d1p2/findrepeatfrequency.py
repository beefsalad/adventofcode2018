#!/usr/bin/python3.7
# finds first duplicated frequency.

import os

# set globals
change = None
changelist = []
n = 0

# frequency starts at 0...stop removing this!
freq = 0
# frequency starts at 0...but if we instantiate now the first check will
# return a false positive!
freqlist = []
# shit portability, still on the to learn list
path = os.getcwd()+"/input.txt"
with open(path) as filepath:
    for change in filepath.readlines():
        change = int(change)
        changelist.append(change)

# print(changelist)
# print(freq)


def check(freq, n):
    freqcount = len(freqlist)
    changecount = len(changelist)
    # print(freq, freqlist, n, len(freqlist))
    while freq not in freqlist and n < freqcount:
        freq = changelist[n]
        freqlist.append(freq)
        print(freq, freqlist)
        n += 1
        print(n)
        if n == changecount:
            n = 0
            return(n, freq)


check(freq, n)
