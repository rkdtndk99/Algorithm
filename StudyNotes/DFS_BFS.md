> [이코테 동영상](https://youtu.be/7C9RgOcvkvo) 보고 정리하는 파이썬 기본 알고리즘 

## Search Algorithm 

- 탐색 == 많은 데이터 중 원하는 데이터만 찾아내는 과정 
- 대표적인 그래프 탐색 알고리즘 == DFS & BFS 
- 자주 나오는 유형 

### Stack 
- **FILO** : 먼저 입력되는 데이터가 나중에 나감
- 입구와 출구가 동일한 형태로 시각화 가능 ex)상자 쌓기 
- `list = []`
- **삽입** : 맨 마지막에 넣기 `append(x)` → O(1)
- **삭제** : 맨 마지막에 있는 원소 삭제 `pop()` → O(1)

### Queue 
- **FIFO** : 먼저 들어온 데이터가 먼저 나감
- 입구와 출구가 모두 뚫린 터널과 같은 형태로 시각화 가능 
- `from collections import deque` → 파이썬에서는 deque 라이브러리 사용 `queue = deque()`
- **삽입** : `append()` → O(1)
- **삭제** : `popleft()` → O(1)
- `reverse` : 역순으로 바꾸기 

### 재귀 함수 
- 자기 자신을 다시 호출하는 함수 
- 파이썬에서는 재귀 깊이 제한이 있기 때문에 무한 반복되지 않고 오류 메시지 뜸
- 재귀함수의 종료 조건 
  - 명시하지 않으면 무한 루프 돌게 됨 
- 함수를 스택에 넣었다가 빼는 것처럼 실제로 함수들이 스택 프레임에 담김
- 가장 마지막에 호출된 함수부터 차례대로 종료됨 (FILO)
- 잘 활용하면 복잡한 알고리즘을 간결하게 작성할 수 있음 
- 모든 재귀 함수는 **반복문**을 이용해서 동일한 기능 구현 가능 

-----

## DFS
- Depth-fist Search (깊이 우선 탐색)
- 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘 
- **스택 자료구조**(or 재귀함수) 사용 
  1. 탐색 시작 노드를 스택에 삽입하고 방문 처리 
  2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 있으면, 그 노드를 스택에 넣고 방문 처리 
  3. 방문하지 않은 인접 노드 없으면 스택에서 최상단 노드 꺼냄 
  4. 2~3의 과정 더 이상 반복할 수 없으면 끝
- 방문 기준이 필요함 ex)번호가 낮은 인접 노드 
```python 
def dfs(graph, v, visited):
  # 현재 노드 방문 처리 
  visited[v] = True 
  print(v, end=' ')
  
  # 현재 노드와 연결된 다른 노드를 재귀적으로 방문 
  for i in graph[v]:
    if not visited[i]: 
      dfs(graph, i, visited) 
 ```
 
 -----

## BFS
- Breadth-first Search (너비 우선 탐색) 
- 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘 
- **큐 자료구조** 사용 
  1. 탐색 시작 노드 큐에 넣고 방문처리 
  2. 큐에서 노드 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드 모두 큐에 삽입하고 방문처리 
  3. 2번 과정 수행할 수 없을 때까지 반복 
- 방문 기준이 필요함 ex)번호가 낮은 인접 노드 
```python 
from collections import deque

def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True 
  
  while queue:
    # 큐에서 원소 하나 뽑아서 출력 
    v = queue.popleft()
    print(v, end=' ')
    
    # 아직 방문하지 않은 인접한 원소들 큐에 삽입 
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
```
