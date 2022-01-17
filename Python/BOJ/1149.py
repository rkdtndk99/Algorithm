import sys
input = lambda : sys.stdin.readline().strip()

n = int(input())
dp = [list(map(int, input().split())) for _ in range(n)]

# 1번째 줄부터 이전 줄에서 가장 적은거 더해 가기
for i in range(1, n):
    dp[i][0] = dp[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = dp[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = dp[i][2] + min(dp[i-1][0], dp[i-1][1])

print(min(dp[n-1]))