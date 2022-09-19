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

# 22-09-19 풀이
n, m, k = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
answer = 0
cnt = 1

for _ in range(m):
	if cnt != 3:
		answer += nums[n-1]
	else:
		answer += nums[n-2]
		cnt = 0
	cnt += 1

print(answer)