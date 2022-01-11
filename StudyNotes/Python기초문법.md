# 파이썬 문법 정리 

> [이코테 동영상](https://youtu.be/m-9pAwq1o3w) 보고 정리하는 파이썬 기본 문법 

</br>

### 수 자료형 

- **정수형** 
- **실수형** : 온점 붙이면 자동으로 실수형으로 변환됨 
  - `round()` : 반올림 함수  
- **지수** : e, E 사용 가능. ex) 1e9 = 10^9 (실수형 데이터로 처리됨) 
- **사칙연산** : 
  - `/` : 나누기. 결과가 실수형 
  - `%` : 나머지
  - `//` : 몫
  - `**` : 거듭제곱 

### 리스트 자료형 

- 데이터를 연속적으로 담아 처리하기 위한 자료형 
- array,linked list, vector와 유사한 기능 지원 
- `list()` or `[]` : 비어있는 리스트 
- 크기가 N이고 모든 값이 0인 1차원 리스트 초기화
  ``` python 
  n = 10 
  a = [0] * n 
  print(a) 
  > [0,0,0,0,0,0,0,0,0,0]
  ```
- **slicing** : 연속적인 위치를 갖는 원소들 가져와야 할 때 → [start : end+1] 
- **comprehension** : 대괄호 안에 조건문과 반복문 적용해서 리스트 초기화하기 
  ```python
  array = [i for i in range(10)] 
  print(array) 
  > [0,1,2,3,4,5,6,7,8,9] 
  
  # NxM 2차원 리스트 초기화 
  array = [[0]*m for _ in range(n)]
  ```


### 문자열, 튜플 자료형 

- `"` or `'` 
- indexing, slicing 가능. 문자열의 특정 인덱스 값을 변경할 수 없음 
- **튜플** : 
  - 한 번 선언된 값 변경 불가능
  - `()`
  - 공간 효율적 
  - *사용* : 
    - **서로 다른 성질**의 데이터 묶어서 관리 → 최단경로에서 비용 or 노드 번호로 사용 
    - 데이터의 나열을 **hashing의 key값**으로 사용할 때 → 변경 불가능하기 때문에 
    - 리스트보다 **메모리 효율적**으로 사용해야할 때 

### 사전 자료형

- [key : value] 쌍을 데이터로 가짐 
- `dict()` : 초기화 
- `keys()` : 키 데이터만 뽑아서 리스트로 이용 
- `values()` : 값 데이터만 뽑아서 리스트로 이용 
- **순서가 없어서 indexing으로 값 얻을 수 없음**

### 집합 자료형 

- 중복 허용 X, 순서 X 
- `set()` : 리스트 혹은 문자열을 이용해서 초기화 
  ```python 
  data = set([1,1,2,3])   # 초기화 방법 1 
  data = {1,1,2,3}        # 초기화 방법 2 
  ```
- 초기화할 때 중복된 원소들은 삭제한 상태로 저장 
- `|` : 합집합 
- `&` : 교집합 
- `-` : 차집합 
- `add()` : 새로운 원소 추가 
- `update([])` : 새로운 원소 여러 개 추가 
- `remove()` : 특정 값 갖는 원소 삭제 
- **순서가 없어서 indexing으로 값 얻을 수 없음**

### 기본 입출력 

- **입력**: 
- `input()` : 한 줄의 문자열 입력 받음 
- `map()` : 리스트의 모든 원소에 각각 특정한 함수 적용할 때 사용 
  - return 자료형이 iterator 
  - `map(적용할 함수, 원소)`
- ex) 공백을 기준으로 구분된 데이터 입력받을 때 
  ```python 
  list(map(int, input().split()))
  ```
- 사용자로부터 입력을 최대한 빠르게 받아야 하는 경우 
  - `sys.stdin.readline()` : sys 라이브러리에 있음 (`import sys`) 
  - `rstrip()` : enter가 줄바꿈 기호로 입력돼서 같이 사용해야함 → 줄바꿈 기호 제거 
  - 이진탐색, 그래프, 정렬 관련 문데에서 자주 사용 

- **출력** : 
- `print()` : 기본적으로 출력 이후에 줄바꿈. `,`로 띄어쓰기 가능 
- `end=" "` : 줄바꿈 원하지 않을 때 
- f-string : 문자열 안에 다른 자료형을 함께 넣을 수 있음 
  ```python 
  answer = 7 
  print(f"정답은 {answer}입니다.")
  > 정답은 7입니다. 
  ```

### 조건문 

- if, elif, else 
- **논리 연산자** : `and`, `or`, `not` 단어 직접 입력 
- **존재 여부 (in 리스트, 튜플, 문자열, 딕셔너리)** : `in`, `not in` 
- `pass` : 아무것도 처리하고 싶지 않을 때 

  ex) 디버깅 과정에서 조건문 처리 부분 비워놓고 싶은 경우 
  
- **조건부 표현식** : if~else 한 줄에 작성 가능 
  ```python 
  score = 85
  result = "Success" if score>=80 else "Fail" 
  print(result) 
  > Success
  ```
  
- 조건문 내 부등식 → 수학의 부등식 그대로 사용 가능 `3 < 4 < 5` 

### 반복문 

- 코테에서는 `while`문보다 `for`문이 간결한 경우가 더 많음 
- `range(start, end+1)` : for문에서 연속적인 값 차례대로 순회할 때 
  ```python 
  sum=0
  for i in range(1, 10):
    result += i 
  print(sum)
  > 45
  ```

### 함수와 람다 표현식 

- 파라미터의 변수를 직접 지정할 수 있음 
  ```python 
  def add(a,b) :
    print('result : ', a + b) 
  
  add(b=3, a=7)   # 매개변수의 순서 달라도 OK 
  > result : 10
  ```
- `global` : 전역변수 함수 내에서 사용할 때 선언 
- 함수는 여러 개의 return 값을 가질 수 있음 → 묶여져서 한 번에 반환(packing) 
- **람다 표현식** : 
  - 특정한 기능을 수행하는 함수를 한 줄에 작성할 수 있음 
  ```python 
  print((lambda a, b : a+b)(3,7)) 
  > 10 
  ``` 
  - 내장 함수에서 잘 사용됨 
  ```python 
  array = [('A', 50),('B', 32),('C', 74)]
  print(sorted(array, key=lambda x : x[1]))    # key는 정렬의 기준이 되는 원소 
  > [('B', 32),('A', 50),('C', 74)]
  ```

### 자주 사용되는 표준 라이브러리 

- 내장함수 : 기본적인 함수들 
  - `sum()`, `min()`, `max()`
  - `eval()` : 수식을 계산해서 출력 
    ```python 
    print(eval("(3+5)*7")
    > 56
    ```
  - `sorted()`, `sorted() with key`
- `itertools` : 반복되는 형태의 데이터 처리하기 위한 기능 제공 
  - 순열
    ```python 
    from itertools import permutations 
    
    permutations(list, n개 골라)
    ``` 
  - 조합 
    ```python 
    from itertools import combinations
    ```
  - 중복순열, 중복조합 
    ```python 
    from itertools import product 
    from itertools import combinations_with_replacement
    ```
- `heapq` : 힙 자료구조 제공. 우선순위 큐 구현 위해 사용 
- `bisect` : 이진탐색 기능 제공 
- `collections` : deque, counter 등의 자료구조 포함 
  - `counter` : 등장 횟수를 세는 기능 제공. 리스트같은 객체 내의 원소가 몇 번씩 등장했는지 알려줌 
  ```python 
  from collections import Counter 
  
  counter = Counter([1, 2, 2, 2, 3, 4, 4]) 
  print(counter[1]) 
  print(counter[4]) 
  print(dict(counter))   # 사전 자료형으로 반환 
  > 1 
  > 2 
  > {1 : 1, 2 : 3, 3 : 1, 4 : 2}
  ``` 
- `math` : 수학적인 기능 제공 
  - 팩토리얼, 제곱근, 최대 공약수, 삼각함수, 파이 등등... 
  - `gcd()` : 최대 공약수 구하기 
  - `lcm()` : 최소 공배수 구하기 
    ```python 
    def lcm(x,y):
      return x*y // gcd(x,y)
    ```

