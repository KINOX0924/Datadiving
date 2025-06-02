# 알고리즘
# 컴퓨터 과학에서 알고리즘은 입력 데이터를 받아 원하는 결과를 출력하는 과정을 말함
# 효율적인 알고리즘은 실행 시간과 자원 사용을 최소화함

# 과거 2세대애에서는 결과 중심주의(데이터) 였으며 대부분의 프로그램 코드가 '스파게티 코드' 였음
# go-to 문이라고 해서 코드 자체가 이리저리 왔다갔다 했음

# 이후 3세대로 가면서 '과정 중심주의(알고리즘)' 와 '모듈화(프로시저, 함수)' 로 진행되었고 go-to 문을 없애거나 줄이면서 스파게티 코드가 줄어듬
# 자료구조는 '데이터' 측면에서 바라본 용어이며 , 알고리즘은 '절차적' 측면에서 바라본 용어이나 둘은 같은 의미를 지님

# 4세대로 오면서 다시 결과 중심주의로 돌아왔으나 알고리즘은 '당연히' 기본적으로 깔린 상태에서 정확한 데이터가 나오는 것을 중심으로 함

# 자료 구조
# 자료 구조는 데이터를 효율적으로 저장하고 관리하는 방법을 말함

# 자료구조는 선형 자료 구조와 비선형 자료 구조로 분류됨
# 선형 자료 구조 : 배열 , 연결 리스트 , 스택 , 큐
# 비선형 자료 구조 : 트리 , 그래프
# * 컴퓨터 입장에서 정적인 자료 구조는 빠른 자료 구조를 말하며 , 동적인 자료 구조는 느린 자료 구조를 말함

# 전통적인 알고리즘
# 링크드리스트 / 스택 / 큐 / 더블 링크드리스트 / 수식 전환
# 해쉬 검색 / 퀵 정렬 / 트리 및 트리 순회

# 변수
# [1] C언어는 값 변수와 포인터형 변수 두 개로 나누어짐
# C 언어의 문제가 특정 변수를 값 타입으로도 선언할 수 있고 포인터 타입으로도 선언할 수 있음, 하지만 장점은 OS 나 그 밖에 시스템 프로그램이 모두 코딩 가능함
# 값 변수 : int a = 6; (a 라는 변수와 값 6 전부 스택에 저장됨)
# 포인터형 변수 : int *p; (값은 넣을 수 없으며 주소만 저장되며 사용하기 위해서는 p = &a; / p = new int; 등으로 사용하며 다른 변수의 주소를 저장하거나 힙 공간에 동적으로 할당을 받아야함)

# [2] JAVA 에서는 포인터형 변수를 없애고 '값타입' 과 '참조타입(포인터)' 를 만듬
# JAVA 의 참조타입에는 배열과 객체만 있고, 나머지는 모두 값 타입의 변수임
# 값타입을 때때로 참조타입으로 전환해야할 경우 wrapper 클래스가 있으며 int 는 값타입이지만 Integer 는 참조타입임

# [3] 파이썬에서는 구분을 없애고 전부 참조타입 변수로 만듬(모든 값이 다 heap 에 저장됨)
# 따라서 장점이 C 언어를 그대로 사용할 수 있음
# 파이썬의 모든 변수는 대상 자체가 아니라 대상이 있는 주소만 저장함, 그래서 변수의 타입을 선언할 필요도 없고 사용 방법도 일관적임

# 파이썬의 객체
# 파이썬의 모든 객체는 세 가지 속성을 지님
# [1] 아이덴티티 : 객체를 고유하게 식별하는 값
# [2] 유형 : 객체가 어떤 조율의 데이터를 가리키는 지 나타내는 정보
# [3] 값 : 객체가 실제로 가지고 있는 데이터

# 배열(Array) 의 본래 특징
# [1] 연속된 메모리 공간
# [2] 정적임 - 프로그램 실핸 전에 메모리 크기 확정, 위치 확정 / 수행 도중에 메모리 크기를 늘리거나 줄이거나 또는 위치 이동 불가능(파이썬, 자바도 이 성격 위배됨)
# [3] 인덱싱으로 요소들에 접근할 수 있음
# [4] 같은 타입이어야 함(파이썬은 값의 주소만 저장하기 때문에 리스트에 다양한 타입의 값을 넣을 수 있음)

# 정수 배열에서 가장 큰 수 두 수를 찾기

"""
def findMax(number_list) :
    for index in range(0 , len(number_list)) :
        for index_2 in range(0 , len(number_list) - 1) :
            if number_list[index] > number_list[index_2] :
                number_list[index] , number_list[index_2] = number_list[index_2] , number_list[index]
    
    print(f"가장 큰 수 : {number_list[0]}")
    print(f"두번째로 큰 수 : {number_list[1]}")

if __name__ == "__main__" :
    number_list = [3,-1,5,0,7,4,9,1]
    findMax(number_list)
"""

# 펠린드롬
"""
word = "racecar"

if word == word[::-1] :
    print(True)
else :
    print(False)
    
print(word)
print(word[len(word) - 1])
    
# 절반을 쪼개서 - 길이로 계산

def palindromes(word) :
    left_word = 0
    right_word = len(word) - 1
    
    while left_word < right_word :
        if word[left_word] != word[right_word] :
            return False
        left_word += 1
        right_word -= 1
    return True

Result = palindromes(word)
print(f"{Result}")
"""

# 연결 리스트
# 데이터를 연속된 메모리 공간에 저장하지 않고, 각 데이터가 다음 데이터의 위치를 가리키는 방식으로 구성된 선형 자료 구조
# 각 데이터 단위를 노드라고 하며, 노트는 데이터를 저장하지 않고 다음 노드를 가리키는 참조(주소) 를 포함
# 자료의 양이 정해져 있지 않거나 추가 및 삭제가 빈번할 때는 연결 리스트가 더 적합
"""
arr = list()

for i in range(0 , 10) :
    arr.append(i + 1)
print(arr)
    
for i in range(9 , 3, -1) :
    arr[i] = arr[i-1]
print(arr)

arr[3] = 88
print(arr)
"""

# 리스트와 노드
"""
class Node :
    def __init__(self , data = None) :
        self.data = data    # 데이터 파트
        self.next = Node    # 다음번 요소의 주소를 줘야함
        
class Mylist :
    # haed 와 tail
    # head : 리스트이 시작을 가리킴
    # tail : 리스트의 마지막을 가리킴
    
    def __init__(self) :
        self.head = Node()  # 사용하지 않음(실 데이터 저장 안함)
                            # head 와 tail 사이에 데이터가 들어감
        self.tail = Node()  # 사용하지 않음(실 데이터 저장 안함)
        self.head.next = self.tail
        self.tail.next = self.tail
        # head -> (|) -> tail(|) -> None
        # head 는 테일쪽(데이터) 을 향해 가리키며 테일은 테일은 가리킴

    def insertHead(self , data) :
        temp = Node(data)
        temp.next = self.head.next
        self.head.next = temp
        
        # head -> temp -> tail
    
    def deleteHead(self) :
        if self.head.next == self.tail :
            return  # 이미 다 삭제되어서 삭제할 것이 없는 경우 단순 리턴
        self.head.next = self.head.next.next
    
    def deleteAll(self) :
        self.head.next = self.tail
        # 파이썬의 경우 메모리 관리를 스스로 하기 때문에 이렇게 가능
    
    # 이 구조는 출력하려는 함수
    def print(self) :
        print(self.head.next.data)
        print(self.head.next.next.data)
        print(self.head.next.next.next.data)
    
    def print_2(self) :
        # head 값과 tail 의 값을 움직이면 안됨/ 절대 바뀌면 안됨
        # 추적용 노드 타입을 선언
        
        trace = self.head.next
        while trace != self.tail :
            print(trace.data)
            trace = trace.next
            
    def insertOrder(self , data) :
        temp = Node(data)
        t1 = self.head.next
        t2 = self.head
        flag = False
        while not flag and t1 != self.tail : 
            if t1.data > temp.data :
                flag = True
            else :
                t1 = t1.next
                t2 = t2.next
                
        temp.next = t1
        t2.next = temp
        
m1 = Mylist()
m1.insertOrder("A")
m1.insertOrder("B")
m1.insertOrder("C")
m1.insertOrder("D")
m1.print_2()

# m1 = Mylist()
# m1.insertHead("A")
# m1.insertHead("B")
# m1.insertHead("C")

# m1.print_2()

# print("삭제하기")
# m1.deleteHead()
# m1.print_2()

# 단일 링크드리스트의 단점은 자신의 앞은 추척이 불가능함
# 뒤를 가리키는 주소가 있기에 뒤는 가리킬 수 있으나 중간에 링크가 끊어지면 그걸로 끝(데이터 추적이 불가)
# 이중 링크드리스트 : prev , next 두 개의 링크를 가지는 링크드리트스
# prev = 앞의 것 , next = 뒤의 것
# 환형 링크드리스트 : 사용하지 않음 / 큐 구조를 만들때 배열의 경우

# 본래의 링크드리스트는 데이터가 정렬이 되어서 들어가야함
# 링크드리스트를 만들때는 [1] 헤드에 아무것도 없을 때 , [2] 리스트의 맨 끝에 데이터가 추가될때 , [3] 중간에 끼워넣을때

class Book :
    def __init__(self , title = "" , author = "" , publisher = "") :
        self.title     = title
        self.author    = author
        self.publisher = publisher
        
        self.next = Book
    
    def __gt__(self , other) :
        if self.title > other.title :
            return True
        return False
    
    def __str__(self) :
        return f"{self.title} , {self.author} , {self.publisher}"
        
m2 = Mylist()
m2.insertOrder(Book("마법사의 돌" , "조앤롤링" , "해냄"))
m2.insertOrder(Book("그리고 아무도 없었다" , "아가사 크러스티" , "해냄"))

m2.print_2()

b1 = Book("쌍갑포차")
b2 = Book("쌍갑포차")

print(b1 == b2)
# b1 과 b2 의 내용 비교가 아니고 , b1 이 참조만 저장 , b2 도 참조만 저장
# 둘이 동일한 객체를 참조하고 있느냐만 비교할 뿐 , 값이 같은 지는 비교하는 것이 아님

s1 = str("hello")
s2 = str("hello")

print(s1 == s2)
# 이 경우는 str 에서 연산자 중복을 지원하기 때문에 참조가 아닌 값을 비교함
"""



# 스텍 구조
# 스텍은 LIFO 구조로 되어있음 - Last in First out
# 인터럽트 또는 함수에 주로 사용
# 인터럽트(가로채기) 
# 수식 트리 , 트리 순회
# push       = 스텍의 마지막에 데이터 삽입
# pop        = 스텍의 마지막에서 데이터 하나 반환
# peek       = 스텍의 마지막을 확인만 함
# isFull     = 스텍이 꽉 차있으면 True , 아니면 False
# isEmpty    = 스텍이 비면 True , 아니면 False
# top 인덱스 = 스텍의 마지막 인덱스를 가리킴

# 내부 데이터는 배열로 사용

class Mystack :
    def __init__(self , size = 10) :
        if size < 10 :
            self.size = 10
        else :
            self.size = size
        self.stack = []
        for i in range(0 , size) :
            self.stack.append(0)
        # 여기서 0 은 값이 비어있음을 의미

        self.top = -1
    
    # 푸시 함수
    # 데이터가 isFull 상태가 아니면 top 증가시키고 그 안에 값을 넣음
    def push(self , data) :
        
        result = self.isFull()
        if result == True :
            return
        # if self.isFull() == True :
        #   return
        
        self.top += 1
        self.stack[self.top] = data
        
    # 팝 함수
    def pop(self) :
        
        if self.isEmpty() == True :
            return None
        
        temp = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        
        return temp
    
    # isFull 스텍에 데이터가 풀인지 아닌지 확인
    def isFull(self) :
        if self.size - 1 == self.top :
            return True
        return False
    
    # 스텍에 데이터가 없는 지 확인
    def isEmpty(self) :
        if self.top == -1 :
            return True
        return False
    
    # 마지막 데이터 값을 보여줌
    def peek(self) :
        if self.isEmpty() :
            return None
        return self.stack[self.top]
    
    def print(self) :
        i = 0
        
        while i <= self.top :
            print(self.stack[i] , end = " ")
            i += 1
        print()

if __name__ == "__main__" :
    s1 = Mystack()
    s1.push("A")
    s1.push("B")
    s1.push("C")
    s1.push("D")
    s1.push("E")
    s1.push("F")
    s1.push("G")
    s1.push("H")
    s1.push("I")
    s1.push("G")
    s1.push("K")
    s1.push("L")
    
    
    s1.print()
    
    print(s1.pop())
    print(s1.pop())
    print(s1.pop())
    print(s1.pop())
    print(s1.pop())
    print(s1.pop())
    print(s1.pop())
    print(s1.pop())
    print(s1.pop())
    print(s1.pop())
    print(s1.pop())
    print(s1.pop())
    print(s1.pop())
    
def reverse(arr) :
    s = Mystack(len(arr))
    
    for i in arr :
        s.push(i)   
        
    result = ""
    while not s.isEmpty() :
        result += s.pop()
    return result

print(reverse("korea"))