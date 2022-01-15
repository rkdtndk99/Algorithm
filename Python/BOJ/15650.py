import itertools
import sys
input = lambda : sys.stdin.readline().strip()

N, M = map(int, input().split())
arr = [int(i)+1 for i in range(N)]
nCm = list(map(' '.join, itertools.combinations(map(str, arr), M)))
for e in nCm:
    print(e)
