from collections import deque
import sys
input = lambda : sys.stdin.readline().strip()


def bfs(x, y):
    queue = deque([(x, y)])
    if x == ex and y == ey:
        return 0
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in [(-2,1),(-1,2),(1, 2), (2,1),(-2,-1),(-1,-2),(2,-1),(1,-2)]:
            nx, ny = cx + dx, cy + dy
            if nx < 0 or nx > N-1 or ny < 0 or ny > N-1:
                continue
            if visited[nx][ny] == 0:
                visited[nx][ny] = visited[cx][cy] + 1
                queue.append((nx, ny))

    return visited[ex][ey]


case = int(input())
for _ in range(case):
    N = int(input())
    visited = [[0] * N for _ in range(N)]

    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    print(bfs(sx, sy))