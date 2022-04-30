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
