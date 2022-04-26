from collections import deque
import sys
input = lambda : sys.stdin.readline().strip()


def bfs():
    queue = deque()
    queue.append(N)
    while queue:
        x = queue.popleft()
        if x == K:  # 해당 수에 도착
            print(visited[x])
            break
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx < MAX and not visited[nx]:
                visited[nx] = visited[x] + 1
                queue.append(nx)


MAX = 100001
N, K = map(int, input().split())
visited = [0] * MAX
