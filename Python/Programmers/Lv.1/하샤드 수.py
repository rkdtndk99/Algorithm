# 내 풀이
def solution(x):
    arr = list(str(x))
    s = sum(map(int, arr))
    if x % s == 0:
        answer = True
    else:
        answer = False
    return answer

# 다른 사람 풀이
def solution(x):
    return x % sum([int(c) for c in str(x)]) == 0