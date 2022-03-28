# 내 풀이
def solution(d, budget):
    answer = 0
    total = 0
    d.sort()
    for i in range(len(d)):
        total += d[i]
        if total <= budget:
            answer += 1
        else:
            break
    return answer

# 다른 사람 풀이
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()

    return len(d)