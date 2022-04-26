import sys
import itertools
input = lambda : sys.stdin.readline().strip()

N, M = map(int, input().split())
arr = [int(i)+1 for i in range(N)]
nPm = list(map(' '.join, itertools.permutations(map(str, arr), M)))
for e in nPm:
    print(e)
