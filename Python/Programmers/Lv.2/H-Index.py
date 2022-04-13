# 내 풀이
def solution(citations):
    count = 0
    citations.sort()
    for i in range(citations[-1] + 1):
        new_c = [item for item in range(len(citations)) if citations[item] >= i]

        if len(new_c) >= i:
            count = i
        else:
            break

    return count

# 다른 사람 풀이
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0