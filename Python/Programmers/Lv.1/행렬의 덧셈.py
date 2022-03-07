# 내 풀이
def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        answer.append([])
        for j in range(len(arr1[0])):
            answer[i].append(arr1[i][j] + arr2[i][j])
    return answer

# 내 풀이2
# 2차원 배열은 초기화할 때 * 쓰면 주소값도 똑같이 복사(?)되는 거라서 for문 써주어야 함 
def solution(arr1, arr2):
    answer = [[0]*len(arr1[0]) for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    return answer


# 다른 사람 풀이
def solution(arr1, arr2):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]
    return answer