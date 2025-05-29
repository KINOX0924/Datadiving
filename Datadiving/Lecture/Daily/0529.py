# # 5월 29일 강의

# # 리플랙션 - 거울
# # 클래스를 만들면 , 언어 번역가들이 클래스 정보를 읽어서 정보를 해석해서 저장하고
# # 그 정보에 접근할 수 있게 해줌
# # 프로그램이 실행 중에 객체 , 클래스 , 함수 등의 정보를 확인하거나 조작하는 기능을 말함
# # 요약하자면 코드가 자기 자신을 들여다보고(거울) 조작할 수 있는 능력

# # 리플랙션 기능은 프레임워크를 만들때 필요함
# # -> 사용자가 클래스를 설계

# import inspect # inspect 라이브러리는 각 요소가 함수인지 아닌지 확인할 수 있음

# class Person :
#     # 생성자에서 두개를 만들었으니 두 개의 필드에 생성된 것
#     def __init__(self , name = "" , age = 20) :
#         self.name = name
#         self.age  = age
    
#     def greet(self) :
#         print(f"Hello , {self.name}")
        
# p = Person("Tom" , 12)


# # 클래스 내의 속성을 가져오는 함수
# a = getattr(p , "name") # 특정 개체로부터 속성을 가져옴
# print(a)

# # dir 명령어를 사용하면 클래스 내부의 구조를 전부 보여줌
# print(dir(p))

# # dir 명령어 - 필터링을 사용해서 사용자가 만든거만 확인
# # 컴프리헨션
# fields = [ x for x in dir(p) if not x.startswith("__")]
# print(fields)

# # 객체에서 속성이나 메서드를 가져오는 함수
# for field in fields :
#     print(getattr(p , field))

# # 특정 개체 안에 있는 모든 메서드와 변수들을 다 가져옴
# # ismethod = 메서드인지 확인
# # isfunction = 함수인지 확인
# print(inspect.getmembers(p))
# for item , value in inspect.getmembers(p) :
#     if inspect.ismethod(value) or inspect.isfunction(value) :
#         print("함수" , item)
#     else :
#         print("변수" , item)

# # 컴프리헨션 조건식 [ 출력변수 for 출력변수 in 변수 if 조건식 ]
# # 변수 이름만 추출하기
# var_fields = [ item for item , value in inspect.getmembers(p)
#                if not (inspect.ismethod(value) or inspect.isfunction(value)) and not item.startswith("__")]
# print(var_fields)

# # 함수 이름만 추출하기
# func_fields = [ item for item , value in inspect.getmembers(p)
#                if (inspect.ismethod(value) or inspect.isfunction(value)) and not item.startswith("__")]
# print(func_fields)


# a = getattr(p , var_fields[0])
# print(a)

# # 가져온 객체의 값을 변경
# setattr(p , "name" , "흠길동")
# setattr(p , "age" , 44)

# print(p.name , p.age)


# # 메서드(함수) 를 가져와서 메서드를 호출하기
# # 기본적으로 함수도 주소라서, 파이썬은 변수들한테 주소를 저장할 수 있음
# # 즉 함수의 주소를 변수에 저장 가능함

# def add(x , y) :
#     return x + y

# a = add
# print(a(5,6))

# method = getattr(p , "greet")
# method()


# # 함수의 매개 변수 를 가져오는 함수
# params = inspect.signature(add)
# print(params)
# print(params.parameters)


# # 리플렉션 예제
# # inspect 를 사용하여 변수 리스트를 출력
# # inspect 를 사용하여 함수 리스트를 출력
# # setattr 을 사용하여 x 에는 값 10 을 넣고 , y 에는 값 5 를 넣기
# # getattr 을 사용하여 각 함수를 호출 주소를 가져와서 호출
# class Mytype : 
#     def __init__(self , x = 0 , y = 0) :
#         self.x = x
#         self.y = y
    
#     def add(self) :
#         return self.x + self.y
    
#     def sub(self) :
#         return self.x - self.y
    
#     def mul(self) :
#         return self.x * self.y
    
# t = Mytype(0,0)

# var_fields = [ item for item , value in inspect.getmembers(t)
#               if not (inspect.ismethod(value) or inspect.isfunction(value)) and not item.startswith("__")]
# print(var_fields)

# func_fields = [ item for item , value in inspect.getmembers(t)
#                if (inspect.ismethod(value) or inspect.isfunction(value)) and not item.startswith("__")]
# print(func_fields)

# # 객체 , 변수명 , 들어갈 값
# setattr(t , "x" , 10)
# setattr(t , "y" , 5)
# print(t.x , t.y)

# p_function_add = getattr(t , "add")
# print(p_function_add())

# p_function_sub = getattr(t , "sub")
# print(p_function_add())

# p_function_mul = getattr(t , "mul")
# print(p_function_add())





# 데이터를 저장하는 구조 _ 크게 나누었을 때
# [1] 선형 구조     - 배열과 링크드리스트
# [1-1] 배열
# - 연속된 메모리 공간을 필요로 함
# - 주기억장치(RAM) 에 연속된 공간이 없으면 할당을 할 수 없음
# - 100 Mb 의 공간이 필요하면 100 Mb 를 줄 수 있어야 함 , 하지만 원하는 공간(메모리) 만큼을 주지 못하면 압축을 함
# - 예:)) 10 , 20 , 30 , 40 = 100 / 이러한 압축하는 것을 단편화라고 함 , 이렇게 단편화를 통해서 OS 가 RAM 에 배당을 함
# - 데이터를 접근할 때 INDEX(색인/방번호) 를 사용하며 접근함
# - (최근은 아님) 본래 배열은 프로그램 시작 전에 메모리(공간) 의 크기를 정확하게 지정해야 하며, 중간에 크기를 바꿀 수 없음
# - 현재에는 과거 배열이라 부르는 것들이 배열은 아니고 INDEX 를 사용한다는 점만 남아있음 * a = [] <- 이것은 엄밀히 말해 배열이 아님

# - 배열의 장점은 첫 시작 위치를 알면 다음번 요소가 바로 옆에 있다는 점 (속도가 매우 빠름)
# - 배열의 단점은 융통성이 없어서 필요할 때 메모리를 늘릴 방법도 없고, 수요가 없어졌을 때 줄일 수도 없어서 필요하다면 미리 크게 확보해둘 필요가 있음
# - 데이터를 중간에 끼워넣을 때 다른 데이터들이 이동을 해야하기에 , 데이터 중간에서 삭제하거나 끼워넣을 때 오버헤드가 발생됨

# [1-2] 링크드리스트
# - 앞서 배열의 단점이 있어서 새로 나온 개념이 링크드리스트
# - 데이터와 다음 번 요소에 대한 '주소' 를 저장함 (항상 주소를 가지고 있어야함)
# - 예:)) 목걸이 공예 : 비즈를 가지고 연결시켜나가는 듯한 개념
# - 필요한 만큼만 만들어서 사용이 가능함
# - 장점 : 데이터를 중간에 삽입하거나 중간에서 삭제하는 것이 매우 쉬움
# - 단점 : 인덱스를 사용할 수 없고 데이터의 접근이 어려움 / 속도가 느림
# - 파이썬의 리스트가 링크드리스트 구조로 만듬(정확히는 배열과 링크드리스트 구조를 합친 것)
# - 실제로 클래스를 만들면 클래스 내부에 배열을 두고 이 내부 배열을 접근하게 하는 수단들 연산자 중복임

# [2] 비선형구조    - 트리 , 그래프
# [2-1] 트리
# - 부모와 자식으로 나누어짐
# - 트리 구조를 전체 한 바퀴 순회하려면 크게 두 가지 방식이 있음(DFS : 깊이 우선 탐색 / STACK 구조 || BFS : 너비 우선 탐색 / 큐 구조)

# [2-2] 그래프
# - 그래프는 전체 망형태의 구조를 말함


# 각각의 데이터 유형에 따라서 순회 방법이 다름(사용자가 클래스 내부 구조를 모두 다 알아야해서 스트레스가 심함)
# 따라서 사용자에게 동일한 접근 방법을 제시하자하여 반복자(iterator) 를 만듬
# [1] 컬렉션류 - 리스트 , 딕 , 튜플 , 셋(sef) 등 그 밖의 라이브러리들
# - 내부데이터 접근 방법은 통일 iterator 를 제공

# 반복자의 목적
# - 사용자가 클래스 내부를 몰라도 동일한 방법으로 리스트 , 딕 , 튜플 등의 데이터에 접근할 수 있게
# 컬렉션 클래스 설계자들이 공통의 인터페이스를 정의해놓고 구현한 것

# a = [10 , 20 , 30 , 40]
# it = iter(a)    # iter = 반복자 객체를 반환함

# # next 함수는 반복자의 현재 위치값을 반환하고 반복자가 다음번 요소로 이동할 수 있게 해주는 함수
# # (파이썬의 경우) 더 이상 읽을 데이터가 없으면 StopIteration 이라고 하는 예외를 발생시킴
# # 그래서 보통은 직접 이렇게 쓰지 말고 for 문을 쓰라고 되어 있음 ( for i in a : 같은 식으로 )
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# b = {"red" : "빨간색" , "blue" : "파란색" , "green" : "초록색"}
# it_2 = iter(b)

# print(next(it_2))
# print(next(it_2))
# print(next(it_2))

# # 반복자를 가져오는 또 다른 방법
# # __ 로 시작하는 함수들은 내부 함수들을 말함
# iterator = a.__iter__()
# print(next(iterator))


# 반복자를 구축하는 방법은 인터페이스 또는 연산자중복이 있음
# 인터페이스 방식은 클래스는 클래스인데 구현 부분이 없는 클래스


# 연산자 중복 방식
class MyType :
    def __init__(self , x = 0 , y = 0) :
        self.x = x
        self.y = y
    
    # 함수와 함수 사이에 + 가 있을 경우의 계산
    def __add__(self , other) :
        return MyType(self.x + other.x , self.y + self.y)
    
    # 함수와 함수 사이에 * 가 있을 경우의 계산
    def __mul__(self , other) :
        return MyType(self.x * other.x , self.y * other.y)
    
    # 이 클래스에서 최종적으로 출력할 형식을 정함
    def __str__(self) :
        return f"MyType(x = {self.x} , y = {self.y})"

m1 = MyType(4 , 5)
m2 = MyType(8 , 9)
# MyType 이라는 위에 정의된 클래스 객체 m1 과 m2 를 매개변수를 초기 생성자의 매개변수를 주어 생성

# m1 과 m2 사이에 *(곱셈) 기호를 주어 m3 에 계산 결과를 주는 데 곱셉이 있으니 MyType 내의 __mul__ 함수 내의
# 값을 리턴하고 m1 의 x 와 m2 의 x 를 곱한 값과 m1 의 y 와 m2 의 y 를 곱한 값을 __str__ 의 형식으로 반환한 후 print 를 사용하면 
# 리턴 값의 형식으로 출력됨
m3 = m1 * m2
print(m3)

# 위의 설명과 비스한 구조로 돌아감 (+) 가 있으니 __add__ 값이 실행됨
m3 = m1 + m2
print(m3)

# 연산자 중복 2
class Mylist :
    def __init__(self , data) :
        self.data = list(data)
    
    # 리스트 형식으로 반환할 즉 최종 반환 형태를 설정한 것이고
    def __str__(self) :
        return f"Mylist({self.data})"
    
    # 기본적으로 클래스는 리스트 , 배열 타입이 아니어서 인덱스 사용이 안되니 인덱스 사용이 가능하도록 하는 것
    def __getitem__(self , index) :
        if index >= 0 and index < len(self.data) :
            return self.data[index]
    
    # 그리고 인덱스를 사용하여 그 인덱스 위치에 값을 새로 넣을 수 있도록 하는 것
    def __setitem__(self , index , value) :
        self.data[index] = value

# m1 은 리스트가 아니며 클래스인 Mylist 타입임
# 하지만 이 Mylist 객체 안에 접근하기 위해서는?
m1 = Mylist((1,2,3,4,5,6))
print(m1)
print(m1[0])

m1[0] = 10
print(m1[0])