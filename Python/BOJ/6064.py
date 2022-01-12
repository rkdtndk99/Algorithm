num = int(input())
for _ in range(num):
    m, n, x, y = map(int, input().split())
    answer = -1
    while x < m*n:
        if(x-y) % n == 0:
            answer = x
            break
        x += m
    print(answer)
