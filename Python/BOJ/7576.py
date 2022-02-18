from collections import deque
import sys
input = lambda: sys.stdin.readline().strip()


def bfs(x, y):
    global answer
    queue = deque([(x, y)])
    if graph[x][y] == -1:
        return
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in [(-1,0), (1,0), (0,1), (0,-1)]:
            nx, ny = cx + dx, cy + dy
            if nx > m or nx < 0 or ny > n or ny < 0:
                continue
            if graph[nx][ny] == 0:
                queue.append((nx, ny))
                graph[nx][ny] = 1
                answer += 1


m, n = map(int, input().split())
graph = [[-1] * m for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, input().split()))


answer = -1
for i in range(n):
    for j in range(m):
        if graph[i][j] != -1:
            bfs(i, j)

# [print(line) for line in graph]
