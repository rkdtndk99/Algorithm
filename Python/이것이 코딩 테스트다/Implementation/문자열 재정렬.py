import sys
input = lambda : sys.stdin.readline().strip()

# 내 풀이
str = list(input())
str.sort()
sum = 0
for s in str:
    print(s)
    if s.isdigit():
        sum += int(s)

print(''.join(str))




# K1KA5CB7