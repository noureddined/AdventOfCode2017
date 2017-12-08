#Day 8-1#
import operator

file = open("inputd8.txt", 'r').readlines()
listx = []
listy = {}

for l in file:
    l = l.replace('\n','')
    listx.append(l.split(" "))

ops = {
"==": operator.eq,
"!=": operator.ne,
"<>": operator.ne,
"<": operator.lt,
"<=": operator.le,
">": operator.gt,
">=": operator.ge
}

for x in listx:
    if x[4] not in listy and x[0] not in listy:
        listy[x[4]] = 0
        listy[x[0]] = 0
    if x[4] in listy and x[0] not in listy:
        listy[x[0]] = 0
    if x[0] in listy and x[4] not in listy:
        listy[x[4]] = 0


print(listy)

for x in listx:
    op = x[5]
    if ops[op](listy[x[4]], int(x[6])):
        if x[1] == 'inc':
            listy[x[0]] = listy[x[0]] + int(x[2])
        else:
            listy[x[0]] = listy[x[0]] - int(x[2])


b = listy[max(listy, key=listy.get)]
print(b)
        
