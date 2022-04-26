n = int(input())
nums = list(map(int, input().split()))
count = 0

def is_prime(x):
    for j in range(2, x):
        if x % j == 0:
            return False
    return True


for i in nums:
    if i == 1:
        continue
    if is_prime(i):
        count += 1

print(count)
