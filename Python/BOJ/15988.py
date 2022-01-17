import sys
input = lambda : sys.stdin.readline().strip()

n = int(input())
dp = [0] * 1000001
dp[1], dp[2], dp[3] = 1, 2, 4
for i in range(4, 1000001):
    dp[i] = dp[i - 1] % 1000000009 + dp[i - 2] % 1000000009 + dp[i - 3] % 1000000009

for _ in range(n):
    num = int(input())
    print(dp[num] % 1000000009)
