import sys
input = lambda : sys.stdin.readline().strip()

# 내 풀이
n = int(input())
arr = list(input().split())

x, y = 1, 1
for d in arr:
    if d == 'D':
        if x + 1 > n :
            continue
        else:
            x = x + 1
    if d == 'U':
        if x - 1 < 1 :
            continue
        else:
            x = x - 1
    if d == 'L':
        if y -1 < 1 :
            continue
        else :
            y = y - 1
    if d == 'R':
        if y+1 > n:
            continue
        else:
            y = y + 1

print(x, y)


# 2022.09.28 풀이
n = int(input())
dir = list(input().split())
x, y = 1, 1

for d in dir:
	if d == "R":
		dx = 0
		dy = 1
	if d == "L":
		dx = 0
		dy = -1
	if d == "U":
		dx = -1
		dy = 0
	if d == "D":
		dx = 1
		dy = 0

	nx, ny = x + dx, y + dy
	if 0 < nx < n and 0 < ny < n:
		x = nx
		y = ny

print(x, y)
# 정답
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)