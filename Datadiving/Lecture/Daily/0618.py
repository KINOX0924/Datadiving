"""
이진탐색트리

이분 검색은 배열을 사용함 , 이진탐색트리는 이분 검색을 응용하여 검색
데이터를 넣어서 트리를 만들 때 순서를 지키면서 만듬

이진(다리가 두개) => Left 와 Right 두 개의 에지를 넣음
- 나보다 작은 값은 왼쪽으로, 나보다 큰 값은 오른쪽으로 이동시킴

예:)) 16 , 8 , 9 , 2 , 4 , 12 , 17 , 21 , 23
-               16
        8               17
    2       9               21
4               12              23
"""

# Dict 을 사용해도 되고 특정 데이터 타입만 저장하고 싶다면 변경하면 됨
class Data :
    def __init__(self , num) :
        self.num = num

# 이진 트리
class TreeNode :
    def __init__(self , data) :
        self.data  = data
        self.left  = None
        self.right = None

class BinarySearchTree :
    # 루트 노드
    def __init__(self) :
        self.root = None
    
    # 데이터 추가
    # root == None 이면 본인이 root 이기에 root 노드를 만들어야 함
    def insert(self , data) :
        if not self.root :
            self.root = TreeNode(data)
            return
            # root 노드를 만들었으면 함수 종료

        # [1] 내 노드가 들어갈 위치를 찾아야함
        # 추적하다 들어가다보면 None 인 곳에 노드를 추가 가능함
        parent  = None
        current = self.root
        
        # current 가 None 이 아닌 동안
        while current :
            if current.data.num == data.num :
                return          # 중복 데이터 배제
            parent = current    # 현재 위치값을 저장하고, 나중에 parent 와 연결을 함
                                # 나보다 작은 값은 왼쪽으로 나보다 큰 값은 오른쪽으로 이동
            if data.num < current.data.num :
                current = current.left
            else :
                current = current.right
        # 터미널 노드는 에지가 없음
        # current 값이 None 일때까지 Left , Right 로 움직이면서 노드를 찾아감. 따라서 뒤에 parent 가 항상 따라가야함
        
        # 노드 만들어서 parent 에 연결하기
        
        newNode = TreeNode(data)
        if data.num < parent.data.num :
            parent.left = newNode
        else :
            parent.right = newNode
    
    # 데이터 검색 함수
    def search(self , key) :
        current = self.root     # 검색 시작 위치
        count   = 0             # 찾은 횟수
        
        while current :
            if key.num == current.data.num :    # 원하는 데이터를 찾음
                return count
            count += 1
            
            if key.num < current.data.num :
                current = current.left
            else :
                current = current.right
                
        return -1
    
    def find(self , key) :
        parent  = None          # 삭제될 노드의 부모와 자식을 연결해야함
        current = self.root     # 삭제될 노드의 위치를 찾음
        
        find = False            # 못 찼음
        
        while current and not find :
            if current.data.num == key.num :
                find = True
            else :
                parent = current
                if key.num < current.data.num :
                    current = current.left
                else :
                    current = current.right
        
        return find , parent , current
    
    def delete(self , key) :
        # 삭제를 하려고 하는 경우에 삭제할 노드를 찾아야함
        if self.root == None :
            return
        
        found , parent , current = self.find(key)
        
        # 삭제 대상이 없는 경우에도 리턴
        if found == False :
            return
        
        # 삭제 대상이 자식 노드가 없는 경우
        # 먼저 삭제 대상이 자식 노드가 없는 지 확인하고 내가 부모 노드의 왼쪽에 있는 지 , 오른쪽에 있는 지 확인 후에 링크 제거
        # [1] 그냥 자신을 삭제하면 됨
        if current.left == None and current.right == None :
            if parent.left == current :
                parent.left = None
            else :
                parent.right = None
            return
        
        # [2] 자식이 둘 중 하나만 있을 때
        if current.left != None or current.right != None :
            if current.left != None :                   # 왼쪽에 자식 노드가 있으면 왼쪽의 자식 노드를 가져오는 것
                if parent.left == current :
                    parent.left = current.left    
            else :                                      # 오른쪽에 자식 노드가 있는 경우
                if parent.left == current :
                    parent.left = current.left
                else :
                    parent.rignt = current.right
            return
            

        # [3] 양쪽 다 자식이 있을 때
        # 트리 전체를 재편해야함 >> 삭제될 대상의 오른쪽 서브 트리에서 가장 작은 대상을 찾아 바꿔치기를 함 ( 작은 대상은 왼쪽에 있기 때문에 탐색은 왼쪽으로만 진행하면 됨 )
        if current.left != None and current.right != None :
            subParent  = current # 삭제 대상
            subCurrent = current.right
            
            while subCurrent :
                subParent  = subCurrent
                subCurrent = subCurrent.left
            
        # 후속자의 자식을 전달함
        if subParent.left == subCurrent :
            subParent.left = subCurrent.right
        else :
            subParent.right = subCurrent.right             
        
    def inorder(self , node) :
        if node == None :
            return
        self.inorder(node.left)
        print(node.data.num)
        self.inorder(node.right)

if __name__ == "__main__" :
    arr = [ 16 , 8 , 9 , 2 , 4 , 12 , 17 , 21 , 23 ]
    
    bst = BinarySearchTree()
    
    for number in arr :
        bst.insert(Data(number))
    
    bst.inorder(bst.root)
    
    print(bst.search(Data(7)))