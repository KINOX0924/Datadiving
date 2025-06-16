"""
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0

5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1

5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
"""

"""
[1] 2차원 배열 전체를 검색해야함 -> 어디가 섬인지 모르니깐 i , j 를 놓고 전체 배열을 검색함
[2] 첫번째 1 을 찾는다. dfs 나 bfs 를 작동함
* 
"""

"""
M = 5   # 열의 개수 = 너비
N = 4   # 행의 개수 = 높이

array = [
    [1 , 0 , 1 , 0 , 0],
    [1 , 0 , 0 , 0 , 0],
    [1 , 0 , 1 , 0 , 1],
    [1 , 0 , 0 , 1 , 0],
]

visited = [ [0] * M for _ in range(N) ]

def printArray(arr) :
    for line in arr :
        print(line)

# 재귀 호출
# 내부 스텍을 사용함
def dfs(y , x) :
    # dfs 가 시작되는 순간 방문을 표시함
    visited[y][x] = 1
    # printArray(y,x)
    
    # 상하좌우대각선(대각선은 북서부터)
    dx = [0 , 0 , -1 , 1 , -1 , -1 , 1 , 1]
    dy = [-1 , 1 , 0 , 0 , 1 , -1 , 1 , -1]
    
    # 8 방향으로 새로운 좌표를 산출함
    # 그래서 이동 가능한지 확인함
    
    for direction in range(len(dx)) :
        ny = y + dy[direction]
        nx = x + dx[direction]
        # 새로운 좌표 ny , nx 가 벽이면 다른 좌표 확인하기
        
        if ny < 0 or ny >= N or nx < 0 or nx >= M :
            continue
            # continue 문은 이 다음 구문을 실행하지 않고 다시 for 문으로 점프함
        
        if visited[ny][nx] == 0 and array[ny][nx] == 1 :
            dfs(ny , nx)    # 새 좌표에서 다시 dfs 탐색을 시작함

def solution(arr , M , N) :
    island_count = 0
    
    for row in range(0 , N) : # 행(높이) 이 먼저 나와야함
        for column in range(0 , M) :
            # 방문한 적이 없고, 그 부분이 섬이어야함 DFS 호출
            if visited[row][column] == 0 and arr[row][column] == 1 :
                dfs(row , column)
                island_count += 1
    
    return island_count

island_count = solution(array , M , N)
print(island_count)
"""

"""
4 6
110110
110110
111111
111101

미로 탐색
"""

"""
from collections import deque
N = 4 # 행의 개수
M = 6 # 열의 개수

array = [
    [1 , 1 , 0 , 1 , 1 , 0],
    [1 , 1 , 0 , 1 , 1 , 0],
    [1 , 1 , 1 , 1 , 1 , 1],
    [1 , 1 , 1 , 1 , 0 , 1]
]

visited = [ [0] * M for _ in range(N) ]

def printArray(array) :
    for rows in array :
        print(rows)

printArray(array)
printArray(visited)

# Queue 를 사용한 탐색
def bfs(y,x) :
    visited[y][x] = 1   # 방문
    dx = [0 , 0 , -1 , 1 ]#, -1 , -1 , 1 , 1] # 좌우
    dy = [-1 , 1 , 0 , 0 ]#, 1 , -1 , 1 , -1] # 상하
    queue = deque()
    
    # [1] 큐에 현재 좌표값을 입력
    queue.append((y,x))
    
    while queue :   # 큐에 탐색할 것이 남아있는 동안 탐색을 계속함
        # 큐에서 좌표값을 하나 꺼내옴
        cy , cx = queue.popleft()   # 큐에 넣을 때 y 값부터 넣었으므로 y 부터 가져옴
        for direction in range(len(dx)) :
            ny = cy + dy[direction]
            nx = cx + dx[direction]
            
            # 새 좌표를 만들고 
            if ny < 0 or ny >= N or nx < 0 or nx >= M :
                continue
            
            if visited[ny][nx] == 0 and array[ny][nx] == 1 :
                # 몇 번 만에 찾았는지 확인이 필요해서 이동한 자릿수마다 카운트 증가
                visited[ny][nx] = visited[cy][cx] + 1
                queue.append((ny,nx))

bfs(0,0)
printArray(visited)
"""

from collections import deque
N = 7 # 행의 개수
M = 7 # 열의 개수

array = [
    [0 , 1 , 1 , 0 , 1 , 0 , 0],
    [0 , 1 , 1 , 0 , 1 , 0 , 1],
    [1 , 1 , 1 , 0 , 1 , 0 , 1],
    [0 , 0 , 0 , 0 , 1 , 1 , 1],
    [0 , 1 , 0 , 0 , 0 , 0 , 0],
    [0 , 1 , 1 , 1 , 1 , 1 , 0],
    [0 , 1 , 1 , 1 , 0 , 0 , 0],
]

visited = [ [0] * M for _ in range(N) ]

def printArray(array) :
    for rows in array :
        print(rows)

# printArray(array)
# printArray(visited)

# Queue 를 사용한 탐색
def bfs(y,x,house_number) :
    visited[y][x] = house_number   # 방문
    dx = [0 , 0 , -1 , 1 ]#, -1 , -1 , 1 , 1] # 좌우
    dy = [-1 , 1 , 0 , 0 ]#, 1 , -1 , 1 , -1] # 상하
    queue = deque()
    count = 1
    
    # [1] 큐에 현재 좌표값을 입력
    queue.append((y,x))
    
    while queue :   # 큐에 탐색할 것이 남아있는 동안 탐색을 계속함
        # 큐에서 좌표값을 하나 꺼내옴
        cy , cx = queue.popleft()   # 큐에 넣을 때 y 값부터 넣었으므로 y 부터 가져옴
        for direction in range(len(dx)) :
            ny = cy + dy[direction]
            nx = cx + dx[direction]
            
            # 새 좌표를 만들고 
            if ny < 0 or ny >= N or nx < 0 or nx >= M :
                continue
            
            if visited[ny][nx] == 0 and array[ny][nx] == 1 :
                # 몇 번 만에 찾았는지 확인이 필요해서 이동한 자릿수마다 카운트 증가
                visited[ny][nx] = house_number
                count += 1
                queue.append((ny,nx))
                
    return count

def solution(arr , M , N) :
    house_number = 1
    house_list = []
    count = 0
    
    for row in range(0 , N) :
        for column in range(0 , M) :
            # 방문한 적이 없으면 BFS 호출
            if visited[row][column] == 0 and arr[row][column] == 1 :
                house_list.append(bfs(row , column , house_number))
                house_number += 1
                count += 1
    
    return count , house_list

print(solution(array , M , N))
print("map")
printArray(array)


print("visited_map")
printArray(visited)

