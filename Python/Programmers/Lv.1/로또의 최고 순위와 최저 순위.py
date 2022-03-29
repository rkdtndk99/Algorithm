# 내 풀이
def solution(lottos, win_nums):
    answer = []
    match = 0
    nomatch = 0
    for item in lottos:
        if item in win_nums:
            match += 1 # number of matching numbers
        elif item == 0 :
            nomatch += 1
    answer.append(7 - (match + nomatch if match+nomatch > 1 else 1))
    answer.append(7 - (match if match >= 2 else 1))
    return answer

# 다른 사람 풀이
def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1

    return rank[cnt_0 + ans], rank[ans]
