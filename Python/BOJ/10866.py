from collections import deque
import sys
input = lambda : sys.stdin.readline().strip()

n = int(input())
dq = deque([])
for _ in range(n):
    op = input()
    if op == "size":
            print(len(dq))
    elif op == "empty":
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif op == "front":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    elif op == "back":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])
    elif op == "pop_front":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())
    elif op == "pop_back":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.pop())
    elif op.startswith("push_front"):
        push = op.split()
        dq.appendleft(push[1])
    elif op.startswith("push_back"):
        push = op.split()
        dq.append(push[1])