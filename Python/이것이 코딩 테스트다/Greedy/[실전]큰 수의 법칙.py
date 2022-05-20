import sys
input = lambda : sys.stdin.readline().strip()

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

arr.sort()
while m > 0:
    for _ in range(k):
        if m == 0:
            break
        answer += arr[n-1]
        m -= 1
    if m == 0:
        break
    answer += arr[n-2]
    m -= 1

print(answer)