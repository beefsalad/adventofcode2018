#!/usr/bin/python3.7
# finds first duplicated frequency.

import os

# frequency starts at 0...stop removing this!
freq = 0
n = 0 

# frequency starts at 0...but if we instantiate now will the first check work? nope!
changelist = []
# shit portability, still on the to learn list
path = os.getcwd()+"/input.txt"
with open(path) as filepath:
    for change in filepath.readlines():
        # hmmmm, do I have to do create changelist from change or can I just append change.....so much lost
        # I don't remember what didn't like change not being int()ed, should research why
        change = int(change)
        changelist.append(change)
changecount = len(changelist)
#print(changelist)
#print(changecount)
#print(freq)


#check freq in freqlist
# if freq not in freqlist
# change frequency
#   the abstraction here is killing me, as soon as I append to the frequency list the conditional is met?

def check (foundfreq, changes, changecount):
    n = 0
    freqlist = []
    while n < changecount:
        foundfreq += changes[n]
        while foundfreq not in freqlist:
            freqlist.append(foundfreq)
            if n == changecount:
                n = 0
    else:
        print(foundfreq, 'foundit')   
        return (freq)



check(freq, changelist, len(changelist))

print('the answer is not 0 and its not 13 or -12, or 576i think its ', freq)
print('and we still arent checking for duplicates...just checking if in the list.  need to seperate it out further somehow...if freq = freqlist(n-1)? hrmph')