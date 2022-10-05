import sys
input = lambda : sys.stdin.readline().strip()

def dfs(x, y):
    # 범위를 벗어나는 경우 바로 STOP
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    # 아직 방문 전인 경우
    if graph[x][y] == 0:
        graph[x][y] = 1     # 방문 처리
        for nx, ny in [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]:     # 상하좌우 위치 재귀적으로 확인
            dfs(nx, ny)
        return True
    return False


n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
count = 0

for i in range(n):
    for j in range(m):
        # 해당 위치에서 DFS 수행. 재귀 빠져나와서 True이면 count 1 증가
        if dfs(i, j):
            count += 1

print(count)

# 2022.10.05 풀이
n, m = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(n)]

def dfs(x, y):
	if x <0 or x >= n or y <0 or y >= m:
		return False
	if graph[x][y] == 0:
		graph[x][y] = 1
		for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
			nx, ny = x + dx, y + dy
			dfs(nx, ny)
		return True
	return False

result = 0
for i in range(n):
	for j in range(m):
		if dfs(i, j) == True:
			result += 1

print(result)
