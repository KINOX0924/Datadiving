"""
스택을 사용한 후위표기식 계산기
강사님 코드
"""
"""
from prac_stack import Mystack

# 연산자를 확인하여 반환하는 함수
def isOperator(word) :
    return word in r"+-*/"

# 공백이면 반환하는 함수
def isSpace(word) :
    return word == " "

# 우선순위를 가져오는 함수
def getPriority(word) :
    if word in r"+-" :
        return 1
    elif word in r"*/" :
        return 2
    else :
        return 0

# infix 수식을 받아서 postfix 수식으로 전환하여 반환하는 함수
def postfix(expr) :
    stack = Mystack(100)
    result = ""
    
    for word in expr :
        # 피연산자일 경우 출력
        if word.isdigit() :
            result += word
        elif isOperator(word) :
            # and 연산은 [1 and 1] 일때만 1(True) 임
            # 대부분의 언어들이 and 앞의 수식 평가가 False 이면 and 뒤의 연산은 수행하지 않음
            # 반대로 or 은 앞의 수식 평가가 True 이면 뒤의 연산은 수행하지 않음
            result += " "
            while not stack.isEmpty() and getPriority(stack.peek()) >= getPriority(word) :
                result += stack.pop()
            stack.push(word)
        else :
            result += word
    
    while not stack.isEmpty() :
        result += stack.pop()
    
    return result

print(postfix("3*5+2"))
"""

"""
데큐 - 양방향 입출력 큐
from collections import deque

dq = deque()
append = 입력
pop    = 출력

"""

"""
트리 구조 구현

노드(Node) : 트리를 구성하는 기본 요소 , 값과 하위 노드를 가리키는 포인터(주소) 를 가짐
간선(edge) : 노드와 노드를 연결하는 선

루트 : 부모 노드가 없는 최상위 노드 , 모든 트리의 루트는 오직 하나
부모 : 자식 노드를 가진 노드
자식 : 부모 노드의 하위 노드
형제 : 부모가 같은 노드
리프 : 자식이 없는 맨 마지막 노드

크기 : 자신을 포함한 모든 자식 노드의 개수
레벨 : 루트 노드부터 특정 노드까지 연결된 간선의 개수
깊이 : 루트 노드부터 특정 노드까지의 거리 , 수치로만 보면 레벨과 같거나 비슷
높이 : 특정 노드에거 가장 깊은 노드까지의 길이
경로 : 한 노드에서 다른 노드로 갈때 거쳐 가는 노드들의 순서
차수 : 자식의 개수

중위 순회
preorder > node > left > right
A -> B -> D -> G -> E -> C -> F

후위 순회
postorder > left > right > node
G -> D -> E-> B -> F -> C -> A

중위 순회
inorder > left - node > right
A -> G -> D -> B -> E -> F -> C
"""
"""
from collections import deque

class Node :
    def __init__(self , data = None) :
        self.data  = data
        # self.edge = []
        self.left  = None
        self.right = None

def inorder(node) :
    if node :   # node 가 None 이 아니면의 의미
        inorder(node.left)
        print(node.data , end = "\t")
        inorder(node.right)

def preorder(node) :
    if node :   # node 가 None 이 아니면의 의미
        print(node.data , end = "\t")
        preorder(node.left)
        preorder(node.right)

def postorder(node) :
    if node :   # node 가 None 이 아니면의 의미
        postorder(node.left)
        postorder(node.right)
        print(node.data , end = "\t")

# 큐를 이용한 레벨 order - 너비 우선 탐색
# [1] 큐를 초기화
# [2] 무조건 큐에 Node 하나를 넣음
# [3] 큐가 비어있지 않는 동안 반복할 것
#       [1] 큐로부터 무조건 하나 가져옴
#       [2] 데이터를 출력
#       [3] 가지고 온 노드의 left 가 None 이 아니면 , 큐에 다시 넣음
#       [4] 가지고 온 노드의 right 가 None 이 아니면 , 큐에 다시 넣음
# [4] 큐가 빌때까지

root = None

def queueOrder(tree) :
    dq = deque()
    dq.appendleft(tree)
    
    while len(dq) > 0 :
        data = dq.pop()
        print(data.data , end = "\t")
        if data.left != None :
            dq.appendleft(data.left)
        if data.right != None :
            dq.appendleft(data.right)

# addNode
# 부모 노드와 원하는 방향을 부여하고 데이터를 주면 그 위치에 노드를 추가하는 함수
# bleft 값이 True 면 부모 노드의 왼쪽에 붙히고 , False 면 오른쪽에 노드를 추가
def addNode(parent = None , bleft = True , data = None) :
    temp = Node(data)
    global root
    
    if parent == None :
        root = temp
    else :
        if bleft :
            parent.left = temp
        else :
            parent.right = temp
    return temp

def makeTree1() :
    root = addNode(None , True , "A")
    
    level1 = addNode(root , True , "B")
    level2 = addNode(root , False , "C")
    
    addNode(level1 , True , "D")
    addNode(level1 , False , "E")
    
    addNode(level2 , True , "F")
    addNode(level2 , False , "G")
    
    return root
"""
"""
[1] 큐 만들기
[2] 큐에 root 노드 추가
[3] 노드가 추가될 위치 찾기
    [3-1] 큐에서 하나 가져옴
    [3-2] 가져온 노드의 left 가 None 이면 여기에 추가하고 나옴
    [3-3] 가져온 노드의 left 가 None 이 아니면 다시 left 값을 다시 큐에 넣음
    [3-4] 가져온 노드의 right 가 None 이면 여기에 추가하고 , None 이 아니면 다시 right 값을 큐에 넣음
    
[4] 모든 요소가 추가될때까지 1번 , 2번 , 3번을 반복
"""
"""
def makeTree2(root_data = "ROOT" , Data_list = []) :
    node_deque = deque()
    data_deque = deque(Data_list)
    
    root = Node(root_data)
    node_deque.appendleft(root)
    
    while len(data_deque) > 0 :
        node = node_deque.pop()
        if node.left == None :
            node.left = Node(data_deque.popleft())
        elif node.right == None :
            node.right = Node(data_deque.popleft())
        
        if node.left != None :
            node_deque.appendleft(node.left)
        if node.right != None :
            node_deque.appendleft(node.right)
    
    return root

if __name__ == "__main__" :
    # tree = Node("A")
    # tree.left  = Node("B")
    # tree.right = Node("C")
    # tree.left.left  = Node("D")
    # tree.left.right = Node("E")
    # tree.right.left = Node("F")
    # tree.right.right = Node("G")
    
    Tree = makeTree2("A" , ["B" , "C" , "D" , "E" , "F" , "G" , "H"])
    queueOrder(Tree)
    
# 트리구조를 탐색할때는 시스템에서 제공하는 큐 또는 스택을 이용하거나 본인이 직접 만들어야 하는데
# 가능하면 어려워서 시스템에서 제공하는 큐를 사용
"""


from prac_stack import Mystack

class Bignumber :
    def __init__(self , number_list) :
        self.number_list = number_list
        self.stack = Mystack()
        self.result_list = []
        
    def schBigNumber(self) :
        count = len(self.number_list) -1
        
        while count > -1 :
            if self.stack.isEmpty() :
                self.stack.push(self.number_list[count])
                self.result_list.append(-1)
                count -= 1
            elif self.number_list[count] < self.stack.peek() :
                self.result_list.append(self.stack.peek())
                self.stack.push(self.number_list[count])
                count -= 1
            elif self.number_list[count] > self.stack.peek() :
                self.stack.pop()
        
        print(self.result_list)

if __name__ == "__main__" :
    number_list = [4,5,3,7]
    
    sb = Bignumber(number_list)
    sb.schBigNumber()