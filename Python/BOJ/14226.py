from collections import deque
import sys
input = lambda : sys.stdin.readline().strip()


def bfs(v):
    queue = deque([])
    queue.append(v)
    while queue:
        x = queue.popleft()


s = int(input())
screen = []
screen[0] = 0
time = 0
