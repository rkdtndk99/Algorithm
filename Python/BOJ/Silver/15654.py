from itertools import permutations
import sys
input = lambda : sys.stdin.readline().strip()

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
new = list( permutations(arr, M))
for i in new:
    print(' '.join(list(map(str, i))))