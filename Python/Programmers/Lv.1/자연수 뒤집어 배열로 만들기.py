# 내 풀이
def solution(n):
    a = list(str(n))
    a.reverse()
    return list(map(int, a))

# 다른 사람 풀이
def solution(n):
    return list(map(int, reversed(str(n))))