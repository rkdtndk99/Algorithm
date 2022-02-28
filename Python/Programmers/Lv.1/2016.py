# 2016년
day = ['FRI','SAT','SUN', 'MON','TUE','WED','THU']
end = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def solution(a, b):
    answer = day[(sum(end[:a-1]) + b-1) % 7]
    return answer

# datetime 라이브러리 사용
import datetime

def solution(a, b):
    date = 'MON TUE WED THU FRI SAT SUN'.split()
    return date[datetime.datetime(2016, a, b).weekday()]