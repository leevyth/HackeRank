#!/usr/bin/python

def displayPathtoPrincess(n,grid):
#print all the moves here
    print(grid)
    for i, j in enumerate(grid): 
        if 'p' in j:
            princess = (i, j.index('p'))
        if 'm' in j:
            mario = (i, j.index('m'))
    distance = (princess[0] - mario[0], princess[1] - mario[1])
    if distance[0] < 0:
        print('LEFT\n' * abs(distance[0]), end ='')
    elif distance[0] > 0:
        print('RIGHT\n' * abs(distance[0]), end = '')
    if distance[1] < 0:
        print('UP\n' * abs(distance[1]), end = '')
    elif distance[1] > 0:
        print('DOWN\n' * abs(distance[1]), end = '')
            
            

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
