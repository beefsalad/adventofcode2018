#!/usr/bin/python3.7
# For example, if you see the following box IDs:

#    abcdef contains no letters that appear exactly two or three times.
#    bababc contains two a and three b, so it counts for both.
#    abbcde contains two b, but no letter appears exactly three times.
#    abcccd contains three c, but no letter appears exactly two times.
#    aabcdd contains two a and two d, but it only counts once.
#    abcdee contains two e.
#    ababab contains three a and three b, but it only counts once.

#Of these box IDs, four of them contain a letter which appears exactly twice, and three of them contain a letter which appears exactly three times. Multiplying these together produces a checksum of 4 * 3 = 12.

#What is the checksum for your list of box IDs?

import os
from typing import Dict
from collections import Counter

twocount = 0 
threecount = 0
path = os.getcwd()+"/input.txt"
with open(path) as filepath:
    for scannedids in filepath.readlines():
        chars = sorted(set(scannedids))
        scannedids = sorted(scannedids)
        for char in chars:
            print(char,' char',)
            #print(scannedids)

            if scannedids.count(char) == 3:
                print(scannedids.count(char))
                threecount += 1
                print('found threse', char,' in', scannedids)
            elif scannedids.count(char) == 2:
                print(scannedids.count(char))
                twocount += 1
                print('found dose', char,' in', scannedids)
    print(twocount, threecount, 'and the checksum is', threecount * twocount)
            #print(scannedids.count('b'))

 #       print(charcount)
        #sortlist = sorted(scannedids)
        # print(sortlist)

    
#print(twocount, threecount, threecount * twocount)   #its not 249 or 1281 and its too low and 12217 (643*19) or 73302 (1286*57) are too high   

   
