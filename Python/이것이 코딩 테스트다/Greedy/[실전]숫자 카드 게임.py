import sys
input = lambda : sys.stdin.readline().strip()

# 내 풀이
N, M = map(int, input().split())
cards = [list(map(int, input().split())) for _ in range(N)]
maxx = 0

for i in range(N):
    temp = min(cards[i])
    if temp > maxx:
        maxx = temp       # max(temp, maxx)로 대체도 가능함

print(maxx)

# 정답
N, M = map(int, input().split())
result = 0

for _ in range(N):
    data = list(map(int, input().split()))
    min_v = min(data)
    result = max(result, min_v)

print(result)