import sys
input = lambda : sys.stdin.readline().strip()

n = int(input())
p = [0] + list(map(int, input().split()))
dp = p

for i in range(1, n+1):
    for k in range(1, i+1):
        dp[i] = min(p[k] + dp[i-k], dp[i])

print(dp[n])