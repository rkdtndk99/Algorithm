import itertools
import sys
input = lambda : sys.stdin.readline().strip()

N, M = map(int, input().split())
arr = [int(i)+1 for i in range(N)]
nRm = list(map(' '.join, itertools.product(map(str, arr), repeat=M)))
for e in nRm:
    print(e)
