# 내 풀이
from math import gcd

def lcm(x, y):
    return x*y // gcd(x,y)

def solution(n, m):
    answer = [gcd(n,m), lcm(n,m)]
    return answer

# 다른 사람 풀이 - 유클리드 호제법
def solution(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer