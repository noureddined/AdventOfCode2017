#Dag5-1#
with open("inputd5.txt", 'r') as f:
    listx = [int(line.strip()) for line in f]

steps = 0
x = 0
while x <= len(listx)-1:

    if listx[x] == 0:
        listx[x] = listx[x] + 1
        steps = steps + 1
        
    else:
        
        listx[x] = listx[x] + 1
        x = (listx[x]-1) + x
        steps = steps + 1
        

print (steps)
