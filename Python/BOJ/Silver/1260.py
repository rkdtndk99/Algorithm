from collections import deque
import sys
input = lambda : sys.stdin.readline().strip()


def dfs(v):
    print(v, end=' ')
    visited[v] = 1
    for i in range(1, N+1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i)


def bfs(v):
    visited = [0] * (N + 1)  # BFS 위해서 초기화하기
    queue = deque([v])
    visited[v] = 1

    while queue:
        k = queue.popleft()
        print(k, end=' ')
        for i in range(1, N + 1):
            if visited[i] == 0 and graph[k][i] == 1:
                queue.append(i)
                visited[i] = 1


N, M, v = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

dfs(v)
print()
bfs(v)