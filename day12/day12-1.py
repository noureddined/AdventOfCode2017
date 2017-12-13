#DAY12#
import re
file = open('day12.txt').readlines()

listx = []
listy = [0]
listz = []

midden = '<(.*?)\>'
for l in file:
    rgx2 = re.compile(midden)
    test = rgx2.sub('', l)
    match = rgx2.findall(test)
    stringfile = test.strip()

    stringfile = stringfile.replace('  ', ',')
    stringfile = stringfile.replace(' ', '')
    listx.append([int(x) for x in stringfile.split(',')])



listcount = True
while listcount == True:
    listleng = len(listy)
#for test in range (0, 13):
    for x in listx:
        for y in listy:
            if y in x:
                for item in x:
                    if item not in listy:
                        listy.append(item)
                        test = len(listy)
                    else:
                        listz.append(item)
                        test = len(listy)
    if listleng == test:
        listcount = False
        
print(len(listy))




    

