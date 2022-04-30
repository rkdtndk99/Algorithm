import sys
input = lambda : sys.stdin.readline().strip()

for k in range(10):
    answer = 0
    temp = []
    len = int(input())
    b = list(map(int, input().split()))

    for i in range(2, len-2):
        if b[i] > b[i-1] and b[i] > b[i-2]:
            if b[i] > b[i+1] and b[i] > b[i+2]:
                answer = max(b[i-2], b[i-1], b[i+1], b[i+2])
                temp.append(b[i] - answer)
                continue

    print('#' + str(k + 1), sum(temp))