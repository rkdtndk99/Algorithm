from itertools import combinations_with_replacement
import sys
input = lambda : sys.stdin.readline().strip()

N, M = map(int, input().split())
arr = [int(i)+1 for i in range(N)]
nHm = list(map(' '.join, combinations_with_replacement(map(str, arr), M)))
for e in nHm:
    print(e)
