# 내 풀이
def solution(n):
    s = sorted(str(int(n)), reverse=True)
    return int(''.join(s))
