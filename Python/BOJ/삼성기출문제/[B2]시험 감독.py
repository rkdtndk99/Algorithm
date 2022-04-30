import sys
input = lambda : sys.stdin.readline().strip()

n = int(input())
arr = list(map(int, input().split()))
b, c = map(int, input().split())
count = len(arr)

for i in range(n):
    arr[i] = arr[i] - b
    if arr[i] > 0:
        if arr[i] % c :
            count += (arr[i] // c) + 1
        else :
            count += (arr[i] // c)

print(count)
