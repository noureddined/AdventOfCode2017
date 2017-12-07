#Day 6-1#
from itertools import *
import copy
from collections import Counter

#li = [0,2,7,0]
with open("inputd6.txt") as f:
    for line in f:
        li = list(map(int,line.split()))
        
mylist = []
mylist.append(li)

count = 0

while count <= len(mylist)-1:
    hoognum = max(mylist[count])
    lid = mylist[count].index(hoognum)

    cycled = cycle(li)
    startat = islice(cycled, lid+1, None)
    count += 1

    seq2 = copy.deepcopy(mylist[count-1])
    mylist.append(seq2)
    mylist[count][lid] = 0

    x = 0
    for x in range(hoognum):
        if (lid+1) > len(li)-1:
            lid = (lid + 1) % len(li)
            mylist[count][lid] = mylist[count][lid] + 1
            lid = lid
        else:
            mylist[count][lid+1] = mylist[count][lid+1] + 1
            lid += 1
    if seq2 in mylist[:-1]:
        print('Steps: '+ str(count))
        break

    else:
        continue
