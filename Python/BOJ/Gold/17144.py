import sys
input = lambda : sys.stdin.readline().strip()

r, c, t = map(int, input().split())
matrix = []
for _ in range(7):
    matrix.append(list(map(int, input().split())))

