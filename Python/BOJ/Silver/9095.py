import sys
input = lambda : sys.stdin.readline().strip()

# DP인지 모르고 푼 풀이
def sol(num):
    for i in range(4, num+1):
        a, b, c = i-3, i-2, i-1
        list.append(list[a] + list[b] + list[c])
    return list[num]

n = int(input())
for _ in range(n):
    num = int(input())
    list = [0, 1, 2, 4]
    print(sol(num))


# 다른 사람이 푼 DP
# T = int(input())
# def sol(n) :
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     elif n == 3 :
#         return 4
#     else :
#         return sol(n-1) + sol(n-2) + sol(n-3)
#
# for i in range(T):
#     n = int(input())
#     print(sol(n))