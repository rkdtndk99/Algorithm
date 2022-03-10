# 내 풀이
def solution(n):
    sqrt = n**(1/2)
    if sqrt.is_integer() :
        return (sqrt+1)**2
    else:
        return -1

# 다른 사람 풀이
def solution(n):
    sqrt = n**(1/2)
    if sqrt % 1 == 0:
        return (sqrt+1)**2
    else:
        return -1