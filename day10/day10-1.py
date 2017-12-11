#Day 10#
from itertools import *

listx = list(range(256))
length = [129,154,49,198,200,133,97,254,41,6,2,1,255,0,191,108]

skip = 0
idx = 0

for x in length:
    leng = x
    if (idx + leng) > len(listx):
        extra = (idx+leng) % len(listx)
        lenlist = len(listx[idx:])
        temp = listx[idx:] + listx[:extra]
        temp = temp[::-1]
        listx[idx:] = temp[:lenlist]
        listx[:extra] = temp[lenlist:]
    else:
        listx[idx:idx+leng] = listx[idx:idx+ leng][::-1]

    idx = (idx + skip + leng) % len(listx)
    skip += 1

print(listx[0]*listx[1])
