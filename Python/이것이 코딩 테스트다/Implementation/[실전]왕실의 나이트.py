import sys
input = lambda : sys.stdin.readline().strip()

now = input()
y = int(now[1])
x = ord(now[0]) - 96
count = 0

dx = [+1, +1, -1, -1, +2, +2, -2, -2]
dy = [+2, -2, +2, -2, -1, +1, -1, +1]
# steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        count += 1

print(count)

# 2022.09.28 풀이
dx = [2, -2, 2, -2, 1, -1, 1, -1]
dy = [1, 1, -1, -1, 2, 2, -2, -2]

knight = input()
row = int(knight[1])
col = ord(knight[0]) - 96
cnt = 0

for i in range(8):
	nx = row + dx[i]
	ny = col + dy[i]
	if 0 < nx <= 8 and 0 < ny <= 8:
		cnt += 1

print(cnt)