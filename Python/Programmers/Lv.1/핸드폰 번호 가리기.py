# 내 풀이
def solution(phone_number):
    answer = phone_number.replace(phone_number[:-4], '*' * len(phone_number[:-4]))
    return answer

# 다른 사람 풀이
def solution(phone_number):
    return "*"*(len(phone_number)-4) + phone_number[-4:]