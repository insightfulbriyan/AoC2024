import itertools
import math

with open('input.txt', 'r') as f:
    f = [list(i) for i in f.read().split('\n')]
    
    antennas = {}
    for x in range(len(f)):
        for y in range(len(f[x])):
            if f[x][y] == '.':
                continue
            if f[x][y] in antennas.keys():
                antennas[f[x][y]].append([x,y])
            else:
                antennas[f[x][y]] = [[x,y]]
    
    
    
    d = len(f)
    nodes = [['- - -' for _ in range(d)] for _ in range(d)]
    for a in antennas:
        combinations = list(itertools.combinations(antennas[a], 2))
        for m,n in combinations:
            dy = (n[1] - m[1])
            dx = (n[0] - m[0])
            
            one = True
            two = True
            i = 0
            while one or two:
                if one and 0 <= m[0] - i*dx < d and 0 <= m[1] - i*dy < d:
                    #print('node 1', m[0]-dx, m[1]-dy)
                    nodes[m[0] - i*dx][m[1] - i*dy] = f'{i, m, n}'
                else:
                    one = False
                if two and 0 <= n[0] + i*dx < d and 0 <= n[1] + i*dy < d:
                    #print('node 2', n[0]+dx, n[1]+dy)
                    nodes[n[0] + i*dx][n[1] + i*dy] = f'{i,m,n}'
                else:
                    two = False
                i+=1
    
    
    
    
    
    cnt =0
      
    for n in nodes:
        for a in n:
            print(a, end='    ')
            if a != '- - -':
                cnt+=1
                #print('#', end='')
            #else:
                #print('.', end='')
        print()
    print(cnt)