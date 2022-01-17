> [이코테 동영상](https://youtu.be/5Lu34WIx2Us) 보고 정리하는 파이썬 기본 알고리즘 

## Dynamic Programming 
- 메모리를 적절히 사용해서 수행 시간 효율성을 비약적으로 향상시키는 방법 
- 이미 계산된 결과는 별도의 메모리에 저장해서 다시 계산하지 않도록 함 
- 일반적으로 2가지 방식으로 구성됨 
  - Top Down (하향식)
    - **Memoization** : 한 번 계산한 결과 메모리 공간에 메모 (== caching)
  - Bottom Up (상향식)
- 특정 문제가 다음의 조건 만족할 때 사용 가능 
  - 최적 부분 구조 (Optimal Substructure) 
    - 큰 문제를 작은 문제로 나눌 수 있음 
    - 작은 문제의 답을 모아서 큰 문제 해결할 수 있음 
  - 중복되는 부분 문제 (Overlapping Subproblem) 
    - 동일한 작은 문제를 반복적으로 해결해야 함 
- ex) 피보나치 수열 - 점화식(인접한 항들 사이의 관계식)으로 표현 가능 
  - 재귀함수로 구현한 피보나치 함수 - 지수 시간 복잡도 `O(2^N)` (중복되는 부분 문제)
  ```python 
  def fibo(x):
    if x == 1 or x == 2:
      return 1
    return fibo(x - 1) + fibo(x - 2) 

  print(fibo(4))
  ```
  - 다이나믹 프로그래밍으로 해결 
  ```python 
  # top down
  d = [0] * 11     # list for memoization

  def fibo(x):
    if x == 1 or x == 2:
        return 1
    
    # 이미 계산한 적 있는 문제면 그대로 반환
    if d[x] != 0:
        return d[x]

    # 아직 계산하지 않은 문제면 피보나치 결과 반환 
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

  print(fibo(10))
  ```
  ```python 
  # bottom up 
  d = [0] * 11
  
  d[1] = 1
  d[2] = 1
  n  = 10
  
  # 피보나치 함수의 반복문으로 구현 
  for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2] 
  
  print(d[n])
  ```
- 
