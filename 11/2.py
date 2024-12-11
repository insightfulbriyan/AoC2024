import sys
from collections import deque
sys.setrecursionlimit(10**6)


DP = {}
def solve(x, t):
    if (x,t) in DP:
        return DP[(x,t)]
    if t == 0:
        ret = 1
    elif x == 0:
        ret = solve(1, t-1)
    elif len(str(x))%2 == 0:
        dstr = str(x)
        ret = solve(int(dstr[:len(dstr)//2]), t-1) + solve(int(dstr[len(dstr)//2:]), t-1)
    else:
        ret = solve(x*2024, t-1)
    DP[(x,t)] = ret
    return ret
with open("input.txt", "r") as f:
    f = [int(i) for i in f.readline().split()]

    print(sum(solve(x, 75) for x in f))

