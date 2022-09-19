import sys
input = lambda : sys.stdin.readline().strip()

# 내 풀이
str = input()
answer = 1
i = 0
while i < len(str):
    if str[i] == '0' or str[i] == '1':
        answer *= int(str[i]) + int(str[i+1])
        i += 1
    else :
        answer *= int(str[i])
    i += 1

print(answer)

# 2022.09.19 풀이
s = input()
nums = list(map(int,list(s)))
answer = nums[0]

for i in range(1,len(nums)):
	if nums[i] <= 1 or answer <= 1:
		answer += nums[i]
	else:
		answer *= nums[i]

print(answer)

# 정답
data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)