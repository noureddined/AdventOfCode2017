#Day 9-1#
import re

file = open("inputd9.txt", 'r').read()

trash = '<(.*?)\>'
cancel = '!.{1}'

stringfile = file
char = '!'
if char in stringfile:
    rgx2 = re.compile(cancel)
    stringfile = rgx2.sub('', stringfile)
    stringfile = stringfile.strip()

char2 = '<'
if char2 in stringfile:
    rgx = re.compile(trash)
    stringfile = rgx.sub('', stringfile)
    stringfile = stringfile.strip()

def createlist(text):
    stuff=""
    count=0
    for char in text:
        if char=="{":
            count += 1
        if count > 0:
            stuff += char
        if char=="}":
            count -= 1
        if count == 0 and stuff != "":
            yield stuff
            stuff=""
        
listx = list(createlist(stringfile))

for x in listx:
    print('dit is x:' + str(x))

#Bereken aantal groups #
def maxDepth(S):
    current_max = 0
    max = 0
    boek = {}
    
    # Traverse the input string
    for i in range(len(S)):
        if S[i] == '{':
            current_max += 1
            max = current_max
            if max in boek:
                count = boek[max] + 1
                boek[max] = count
            else:
                count = 1
                boek[max] = count

        elif S[i] == '}':
          current_max -= 1

    #check for unbalanced string
    if current_max != 0:
        return -1

    som = 0
    for x in boek:
        depth = x
        aantal = boek[x]
        totaal = depth * aantal
        som += totaal
    return som

totalscore = 0
for y in listx:
    score = maxDepth(y)
    totalscore = totalscore + score

print(totalscore)    


