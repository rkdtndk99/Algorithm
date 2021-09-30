# C++로 알고리즘 시작하기

### 1. C++에 대해서

- 입출력 : cin, cout
    - <iostream> header
    - 상대적으로 느림 → but **Fast I/O** 로 속도 문제 해결 가능!
    - 포맷 지정자를 사용할 필요 없음

### 2. C++ Fast I/O

why? 프로그램 실행 시간의 상당 부분 차지

※ scanf/printf 사용하기 → <iostream>에 <cstdio> 추가되어 있음

1. sync 끊어주기 
    - cin/cout 느린 이유 : 
    c와 c++의 입출력 버퍼를 동기화시켜야 하기 때문 + cin&cout은 tie 관계라서 입력이 들어오기 전 모든 출력을 방출
    
    ```cpp
    void init(){
    	cin.tie(0);
    	cout.tie(0);
    	ios_base::sync_with_stdio(false);
    }
    ```
    
    - 위의 코드로 동기화 해제 & untie
    - 대신 scanf/printf  cin/cout 혼용하면 안됨
2. endl 대신 '\n' 사용하기 
    - endl : 출력 버퍼에 쌓인 내용을 한꺼번에 출력(flush)하는 역할을 해서 오래 걸림

### 3. C++ STL

**STL : Standard Template Library** 

- **컨테이너 :** 데이터 저장 객체(vector, pair, deque, list, set, map, stack...)
- **알고리즘 :** 검색(loswer_bound(), upper_bound(), binary_search()) or 정렬(sort())
- **반복자 :** 컨테이너 순회를 위한 일반화된 방법 제공
- **함수자**

### Container

1. Vector 
    
    동적 배열, 삽입 순서에 따라 상대적인 위치. 인덱스 통해 접근 가능 
    
    ```cpp
    #include <vector> 
    
    vector<class or type> name; 
    
    vector<int> v;   //int형 자료 담은 벡터 
    vector<int> v(4);   //크기가 4인 int형 벡터
    vector<int> v = {3, 4, 7};   //생성과 초기화
    vector<int> v[1001];   //int형 벡터 배열 생성 - tree 만들때 자주 사용
    vector<vector<int>> v;   //2차원
    vector<pair<int, long long>> v;   //pair 자료구조 담은 벡터  
    ```
    
    - 벡터 순회하기
        1. v[i] 형태로 벡터의 값에 접근하기 
            
            ```cpp
            for(int i =0; i<v.size();i++){
            	cout << v[i] << '\n';
            }
            ```
            
        2. 시작과 종료조건 필요 x. 배열 요소 값을 변경할 수 x 
            
            ```cpp
            for(auto i:v){
            	cout << i << '\n';
            }
            ```
            
    - 언제 써?
        - 트리나 그래프의 구조 표현할 때
        - 동적 배열 자료구조가 필요한 모든 상황
2. Stack 
    
    LIFO 
    
    ```cpp
    #include<stack> 
    
    stack<class or type> name; 
    
    stack<int> s;  
    stack<long long> s; 
    ```
    
    - 언제 써?
        - 짝 맞추기 문제에 많이 쓰임 (ex. 백준 #3986)
3. Queue
    
    FIFO 
    
    ```cpp
    #include<queue> 
    
    queue<class or type> name; 
    
    queue<int> q;  
    queue<pari<int, int>> q; 
    ```
    
    - 언제 써?
        - 원형 큐 사용 (ex. 백준 #1158)
        - 순서를 고려한 작업이 필요할 때
        - BFS (넓이 우선 탐색)
4. Pair
    
    데이터 쌍을 표현할 수 있음. 짝을 이루는 데이터를 표현할 때 사용. 
    
    ```cpp
    //3개 헤더 중 아무거나 하나 추가해서 사용 
    #include <utility> 
    #include <vector> 
    #include <algorithm> 
    
    pair<class or type, class or type> name; 
    
    pair<int, int> p; 
    pair<int, Person> p; 
    ```
    
    - 언제 써?
        - 가중치가 있는 그래프를 표현할 때 **벡터**와 함께 사용 
        → 다익스트라 문제 해결할 때
            
            ```cpp
            vector<pair<int(node), int(weight)>> v[MAX_SIZE];
            ```
            
        - element 우선순위 표현할 때 사용
        - 다른 컨테이너(queue, vector, map 등)들과 함께 사용하는 경우 많음
5. Map
    
    key와 value가 쌍으로 저장되며 key로 value에 접근
    
    key는 중복되지 않고 오름차순으로 정렬되어 저장됨 
    
    ```cpp
    #include <map> 
    
    map<class or type, class or type> name; 
    
    map<int, int> m1; 
    map<long, string> m2; 
    ```
    
    - 언제 써?
        - 특정 키워드에 대한 정보를 저장하고 빠르게 참조해야 할 때 (ex. 백준 #4358)
6. Set 
    
    원소의 중복을 허용하지 않음. 자동적으로 정렬된 상태를 유지. 
    수학에서의 집합이라고 생각.
    
    ```cpp
    #include <set> 
    
    set<class or type> name; 
    ```
    
    - 언제 써?
        - 요소들을 중복되지 않게, 정렬된 상태로 저장하고 싶을 때
        - 중복 요소 없는 vector를 만들고 싶을 때 assign() 메소드와 함께 사용
            
            ```cpp
            v.assign(InputIterator first, InputIterator last);
            ```
            

### Iterator

컨테이너에 저장된 원소를 순회하고 접근하는 일반화된 방법을 제공 

컨테이너와 알고리즘이 하나로 동작하게 묶어주는 인터페이스 역할 (컨테이너 전용 포인터)

- 순회
    1. container<type>::iterator 사용해서 (*)붙여 컨테이너 내 요소에 접근 
        
        ```cpp
        vector<int>::iterator iter; 
        for(iter=v.begin(); iter!=v.end(); iter++){
        	cout << *iter << ' ';
        }
        ```
        
    2. auto(타입 추론)을 통해 더 간단하게 작성 가능 
        
        ```cpp
        for(auot iter=v.begin(); iter!=v.end(); iter++){
        	cout << *iter << ' ';
        }
        ```
        

### Algorithm

`#include <algorithm>`

1. 퀵 정렬 → `sort(s, e, function)`
    
    배열 : `sort(arr, arr+length, function)`
    
    벡터 : `sort(v.begin(), v.end(), function)`
    
    **function** → `#include <functional>`
    
    `less<type>` : 오름차순 
    
    `greater<type>` : 내림차순 
    
2. 합병 정렬 → `stable_sort(s, e, funtion)`
3. 이분 탐색 → `binary_search(s, e, val)`
4. 구간 내 val 이상인 첫 값의 위치 → `lower_bounds(s, e, val)`
5. 구간 내 val 초과하는 첫 값의 위치 → `upper_bounds(s, e, val)`
