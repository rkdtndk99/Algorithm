E, S, M = map(int, input().split())

answer = 1
while True:
    # 배수가 되는 수에서 빼고 그 다음 나머지 계산
    if (answer - E)%15 == 0 and (answer - S)%28 == 0 and (answer - M)%19 == 0:
        print(answer)
        break
    answer+=1