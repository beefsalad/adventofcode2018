#!/usr/bin/python3.7
# calculates freq skew.
import os
# shit portability, on the to learn list
path = os.getcwd()+"/input.txt"
print(path)
freq = 0
change = 0
with open(path) as filepath:
    for change in filepath.readlines():
        change = int(change)  # hmmm should be a way to readlines as ints?
        freq += change
print(freq)
