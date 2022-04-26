import sys
input = lambda : sys.stdin.readline().strip()

n = input()
answer = 0
length = len(n) - 1
for i in range(length):   # i는 0부터 시작 ~ 자릿수보다 하나 작은거까지
    answer += (i+1) * 9 * (10 ** i)

answer +=  (length + 1) * ((int(n) - (10 ** length)) + 1)
print(answer)

