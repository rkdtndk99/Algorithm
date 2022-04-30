from collections import deque
import sys
input = lambda : sys.stdin.readline().strip()


def bfs(x, y):
    queue = deque()
    # 처음 큐에 (0, 0) 넣기
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for nx, ny in [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]:
            # 범위 벗어나면 멈추기
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 갈 수 없는 곳이면 멈추기
            if graph[nx][ny] == 0:
                continue
            # 갈 수 있으면 이전 숫자와 더하기
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n-1][m-1]


n, m = map(int, input().split())
count = 0
graph = [list(map(int, input())) for _ in range(n)]
print(bfs(0, 0))


