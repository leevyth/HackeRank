#!/usr/bin/python

def displayPathtoPrincess(n,grid):
#print all the moves here
    for i, j in enumerate(grid): 
        if 'p' in j:
            princess = (i, j.index('p'))
        if 'm' in j:
            mario = (i, j.index('m'))
    distance = (princess[0] - mario[0], princess[1] - mario[1])
    if distance[0] < 0:
        print('LEFT' * abs(distance[0]))
    elif distance[0] > 0:
        print('RIGHT' * abs(distance[0]))
    if distance[1] < 0:
        print('UP' * abs(distance[1]))
    elif distance[1] > 0:
        print('DOWN' * abs(distance[1]))
            
            

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
