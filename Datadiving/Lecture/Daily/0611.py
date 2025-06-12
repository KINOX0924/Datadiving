"""
그리디 알고리즘 [3]

배낭 문제
각 아이템은 무게 w , 가치 y 를 가진다. 배낭에 담을 수 있는 최대 무게는 W 이다.
아이템은 쪼개서 담을 수 있을 때, 최대 가치를 구하시오.
* 최대 , 최소 등의 단어가 나오면 그리디 알고리즘이라고 생각하면 됨

W = 50
items = [(60,10) , (100,20) , (120,30)]
(value , weight)

이 때 아이템은 분할해서 넣을 수 있다.
가치를 최대로 담았을 때 어느 정도까지 담을 수 있는가?
Value = 아이템을 배낭에 넣었을 때 얻게 되는 이익
weight = 아이템의 무게

목적 : 배낭에 담을 수 있는 아이템들의 총합 중 총 가치의 합을 최대화하는 것
가치 / 무게 비율로 아이템 정렬(내림차순)
Kg 당 가치를 구해서 그거부터 다 담는다.
하나씩 넣되, 전체를 다 넣을 수 없으면 용량만큼 비례해서 담는다.
누적 가치 합산 -> 최종 정답
"""

"""
def knapsack(items , W) :
    # 가치밀도 기준 내림차순 정렬
    items.sort(key = lambda x : x[0]/x[1] , reverse = True)
    print(items)
    value = 0
    
    # 차례대로 배낭에 담기
    for i in range(0 , len(items)) :
        
        if items[i][1] < W :
            value = items[i][0]
            W -= items[i][1]
        else :
            # KG 당 가치는 가치/무게
            kg = items[i][0]/items[i][1]
            value += kg * W
            W -= W
            break   # 무게가 초과되면 break 를 사용하여 탈출
    
    return value

print(knapsack([(120,30) , (60,10) , (100,20)] , 50))
"""

"""
이분 검색
- 이분 검색은 검색 전 반드시 정렬이 되어 있어야 함

a = [1,2,3,4,5,6,7,8,9,10]
key = 8

[1] 중간값 : 4번방 > 5 의 값이 key 보다 낮으니깐 1~4 가 든 방은 버림
[2] 다시 6 과 9번방 사이의 중간값이 8 인데 key 와 같음 => 출력

left  = 0
right = 9

mid = (left+right) // 2
* 만일 값이 키값보다 크면 a[mid] > key 이면 left = mid + 1
* 만일 값이 키값보다 작으면 a[mid] < key 이면 right = mid -1

* 찾았던지(key 값과 a[mid] == key) , left <= right
"""

"""
class BinarySearch :
    def __init__(self , num_list , key) :
        self.num_list   = sorted(num_list)
        self.key_num    = key
    
    def search(self) :
        left = 0
        right = len(self.num_list) - 1
        mid = (left + right) // 2
        
        while left <= right :
            if self.num_list[mid] == self.key_num :
                return mid
            elif self.num_list[mid] < self.key_num :
                left = mid + 1
            elif self.num_list[mid] > self.key_num :
                right = mid - 1
                
            mid = (left + right) // 2

        return None

if __name__ == "__main__" :
    num_list = [10 , 9 , 8 , 5 , 1 , 3 , 2 , 4 , 11 , 7 , 6]
    key      = 1
    
    B1 = BinarySearch(num_list , key)
    key_index = B1.search()
    if key_index == None :
        print("KEY 값은 해당 리스트에 존재하지 않습니다.")
    else :
        print(f"{key} 의 인덱스 : {key_index}")
"""

"""
해시 테이블
- KEY 와 VALUE 로 구분된 테이블로 파이썬에서는 딕셔너리 라고 사용되는 것과 같음
- 해시 테이블이란 특정 값이 들어오면 컴퓨터 메모리로 맵핑시키는 함수를 말함
- 맵핑 함수 = 해시 함수
- ASCII 코드로 만들어서 다 더한 다음에 충돌이 나면 안되기 대문에 수식을 통해서 특정값이 나오게 한 다음에 % 키의 전체 개수의 나머지를 사용

* 값 => 해시 함수 => (특정 메모리로 이동) => 해쉬 테이블에 저장
* 해시 테이블의 구축하는 방법은 다양함 : 배열 / 배열과 링크드리스트 / 링크드리스트
* Bucket 의 크기는 대충 전체 키 값 개수의 1/2 에서 1/3 이 가장 적합함

위와 같은 방식으로 만들면 충돌이 일어남


- 처음 해시 테이블 구축 시간이 오래걸린다. 하지만 해시 테이블을 구축하고 나면 검색 속도가 매우 빠름
- 해시 조인은 데이터가 대용량이고 배치처리(한번에 일감을 모아서 처리하는 방식) 방식에 유리함 - 해시 조인 <=> 온라인처리(실시간 처리)
- 보통의 경우는 실시간 처리(일감이 소량으로 여러번 처리 될 경우) - Nested 조인
- nested Loop join(for 문 돌림) - 실시간 처리 // hash join(해시 조인) - 배치 처리
"""

"""
해쉬 함수 만들기
- school 이라는 각 문자별로 unicode 만들어서 더해서 총합 만들기
- 파이썬에서 문자의 unicode 는 ord 함수
"""
"""
# 노드
# 노드를 만드는 클래스
class Node :
    def __init__(self , key = None , value = None) :
        self.key   = key
        self.value = value
        self.next  = None

# 헤드 노드
# 헤드 노드를 사용하여 데이터를 조작함
class HeadNode :
        def __init__(self) :
            self.head = Node()
            self.tail = Node()
            self.head.next = self.tail
            self.tail.next = self.tail
        
        # TODO 키와 밸류는 들어감 / 하지만 키가 중복값일 경우에는 어떻게 처리하는가?
        # TODO 해당 노드의 모든 key 를 확인해서 중복이면 키에 값만 변경되고 , 중복이 아니어야만 새로운 노드를 추가함
        # OPTIMIZE 임시 노드에 헤드를 넣음 => 임시 노드의 끝이 tail 을 가리킬때까지 이동
        # OPTIMIZE 만약 tail 로 이동하는 사이에 Key 값이 같은 것을 만나면 값만 변경하고 return
        # OPTIMIZE 같은 Key 가 없다면 새로운 노드를 만들고 뒤에 추가함
        def insertData(self , key , value) :
            temp_node = self.head
            while temp_node.next != self.tail :
                if temp_node.next.key == key :
                    temp_node.next.value = value
                    print(f"변경값 : {key} , {value}")  #FIX 디버깅
                    return
                temp_node = temp_node.next
            
            new_data = Node(key , value)
            new_data.next = self.head.next
            self.head.next = new_data
            print(f"기존값 : {key} , {value}")          #FIX 디버깅
        
        def getValue(self , key) :
            temp_node = self.head
            while temp_node.next != self.tail :
                if temp_node.next.key == key :
                    return (temp_node.next.key , temp_node.next.value)
                temp_node = temp_node.next
            
            print("찾는 값이 없습니다.")
            return None

        def delValue(self , key) :
            temp_node = self.head
            while temp_node.next != self.tail :
                if temp_node.next.key == key :
                    temp_node.next = temp_node.next.next
                    return
            
            print("삭제할 값이 없습니다.")
            return
        
# 키를 받아서 키를 해쉬코드로 변경하는 클래스
class TransHash :
    def __init__(self) :
        self.key_string = ""
        self.hash_number = 0
    
    def getHash(self , key_string) :
        self.key_string = key_string
        
        for char in self.key_string :
            self.hash_number += ord(char)
            
        return self.hash_number

# 입력받은 테이블 사이즈만큼의 헤드 노드를 만들어서 해시 테이블을 작성
class HashTable :
    def __init__(self , table_size = 100) :
        if table_size < 100 :
            self.hash_table = [HeadNode() for _ in range(100)]
        else :
            self.hash_table = [HeadNode() for _ in range(table_size)]
        self.divider = 100
        print(self.hash_table)          #FIX 디버깅
    
    def insertHashData(self , key , value) :
        trans = TransHash()
        hash_code = trans.getHash(key)
        
        self.hash_table[hash_code % self.divider].insertData(key , value)
        
    def searchHashData(self , key) :
        trans = TransHash()
        hash_code = trans.getHash(key)
        
        search_Data = self.hash_table[hash_code % self.divider].getValue(key)
        
        return search_Data
        
if __name__ == "__main__" :
    T1 = HashTable()
    T1.insertHashData("school" , 13)    #TODO 기존값
    T1.insertHashData("school" , 16)    #TODO 변경값
    T1.insertHashData("cshool" , 1)     #TODO 새  값
    
    Data = T1.searchHashData("cshool")
    print(Data)
"""
# map 은 list 의 요소에 앞에서 전달해준 수식 또는 함수를 적용
# map , filter , range 등등들은 for 문 안에서 호출하거나 리스트로 감싸주어야 작동을 함
"""
6 6
011111
010001
010101
010100
000110
111110

6 6
0 1 1 1 1 1
0 1 0 0 0 1
0 1 0 1 0 1
0 1 0 1 0 0
0 0 0 1 1 0
1 1 1 1 1 0
"""



# N , M = map(int , input().split())
# print(N , M)
# arr = []
# for i in range(N) :
#     arr.append(list(map(int , input().split())))
"""
N , M = ( 6, 6 )
arr = [
    [0, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 0]
]
    
def printArray(arr , N) :
    for i in range(0 , N) :
        print(arr[i])
        
visited = [[False] * M for _ in range(N)]

# 깊이우선탐색(DFS)
def dfs( y , x ) :
    # 매개변수로 전달받는 좌표는 현재의 위치값
    visited[y][x] = True    # 방문했다는 표시
    
    # 현재 좌표로부터 4 방향 내지는 8방향을 확인해 볼 수 있음
    dx = [-1 , 1 , 0 , 0]   # 좌우  // 대각선일 경우에는 dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [0 , 0 , -1 , 1]   # 상하  // 대각선일 경우에는 dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    for i in range(len(dx)) : 
        # 새로운 좌표점을 찾음
        # 새 좌표점이 벽일수도 있고 , 이미 방문했던 곳일수도 있음
        nx = dx[i] + x
        ny = dy[i] + y
        
        if not(0 <= nx < N and 0 <= ny < M) or arr[ny][nx] == 1 :
            continue
        if not visited[ny][nx] :    # 아직 방문하지 않았으면
            dfs(ny , nx)
    
if __name__ == "__main__" :
    printArray(arr , N)
    printArray(visited , N)
    
    dfs(0 , 0)
    printArray(visited , N)
"""
from collections import deque

N , M = map(int , input().split())
arr = []

for i in range(N) :
    temp = list(input())    # str -> list
    temp = list(map(int , temp))
    
    arr.append(temp)
    
visited = [ [False] * M for _ in range(N) ]
    
def printArray(arr , N) :
    for i in range(N) :
        print(arr[i])

# bfs 는 Queue 를 사용한 탐색 기법
def bfs( y , x ) :
    dx = [ -1 , 1 , 0 , 0 ]
    dy = [ 0 , 0 , -1 , 1 ]
    
    visited[y][x] = True
    
    queue = deque()
    queue.append((y,x))
    
    while queue :   # 큐가 빌때까지
        y , x = queue.popleft()
        for i in range(len(dx)) : 
            nx = dx[i] + x
            ny = dy[i] + y
            
            if not ( 0 <= nx < N and 0 <= ny < M ) or arr[ny][nx] == 1:
                continue
            if not visited[ny][nx] :
                visited[ny][nx] = True
                queue.append((ny,nx))

if __name__ == "__main__" :
    printArray(arr , N)
    bfs(0 , 0)
    
    printArray(visited , N)