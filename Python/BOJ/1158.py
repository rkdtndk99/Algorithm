from collections import deque
import sys
input = lambda : sys.stdin.readline().strip()

n, k = map(int, input().split())
ans = []
dq = deque([int(i)+1 for i in range(n)])

while dq:
    dq.rotate(-(k-1))
    ans.append(str(dq.popleft()))

print("<" + ', '.join(ans) + ">")



