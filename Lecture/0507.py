# 5월 7일 강의
# 함수의 지역변수
# 함수 내부에서 변수에 값을 할당하는순간 별도의 변수가 만들어짐
# 예외적으로 외부 변수를 같이 사용하고 싶다면 global 을 앞에 붙임
# 가능하면 적게 사용하는 것이 좋음
"""
global_x = 10

def myfunc() :
    global_x = 30   # 이 때의 global_x 는 지역 변수이므로 외부에 선언되었던 global_x 와는 다른 변수임
    y = 20
    print(global_x , y)

global_x = 100
myfunc()

print(global_x)
"""

# 함수의 매개변수 기본값
# dict 타입으로 받을 때도 호출하는 방식은 유사함
# 실행할 때 함수가 결정되는 방식을 동적결정이라고 함
# 컴파일러 언어의 경우에는 컴파일 시간과 실행시간으로 나뉨
# 컴파일 시간에 결정되면 정적할당 , 실행시간에 결정되면 동적할당이라고 함
# 자바는 컴파일러임에도 불구하고 동적할당 , 파이썬 모든 것이 실행시간에 결정됨(동적 할당)
"""
def myfunc2(name="홍길동" , age=21 , phone="010-0000-0001") :
    print(name)
    print(age)
    print(phone)

myfunc2()
myfunc2("임꺽정",33,"010-0000-0002")
myfunc2(name="둘리")
myfunc2(age=23)
myfunc2(phone="010-0000-0003")
"""

# 제너레이터 (개념)
# 값을 하나씩 생성해서 순회할 수 있는 함수나 객체(대표적으로는 ragne 또는 filter)

# range : for 문 안에서 호출하면 데이터를 한 개씩 만들어서 출력
# 함수 안에서 값을 반환하려면 return 과 yield 가 있음
# return = 값을 반환하면서 함수를 종료함

# yield  = 값을 반환은 하지만 함수는 종료하지 않음
# 데이터가 너무 커서 한 번에 생성할 수 없을 때 사용
# 무한한 작업이 필요할 때
# 파일을 계속 읽어서 처리하고자 할 때
# 이 때 제네레이터 객체가 따로 생성됨 , 내부적으로 파이썬이 일반 함수를 제너레이터 객체로 만들어서 객체 참조를 변수(gen) 으로 전달
"""
def myrange(start=1 , end=5) :
    i = start
    while i <= end :
        yield i     # 해당 구문을 마나는 순간 값을 하나 반환하고 멈춤(함수가 종료된 것은 아님)
        i = i + 1

gen = myrange()     # 함수를 호출해서 결과를 저장
                    # next 구문을 사용하여 차례차례 호출함
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

for i in myrange(1,10) :
    print(i)
"""

# 입력화면 : 원의 면적(1) , 사각형 면적(2) , 사다리꼴 면적(3) , 종료(0)
# (1) 누르면 반지름 입력 나오고 면적은 반지름 * 반지름 * 3.14 = 면적은 XX 입니다.
# (2) 누르면 가로 입력 , 세로 입력 후 면적은 XX 입니다.
# (3) 아랫변 , 윗변 , 높이 나오고 면적
# (4) 는 종료

"""
def calCircle() :
    radius = int(input("반지름을 입력해주세요(cm) : "))
    
    circle = (radius * radius) * 3.14
    print(f"원의 면적은 {circle} cm2 입니다.")

def calQuadrangle() :
    width = int(input("가로 길이를 입력해주세요(cm) : "))
    height = int(input("세로 길이를 입력해주세요(cm) : "))
    
    quadrangle = width * height
    print(f"사각형의 면적은 {quadrangle} cm2 입니다.")

def calTrapezoid() :
    upperWidth = int(input("윗변 길이를 입력해주세요(cm) : "))
    lowerWidth = int(input("아랫변 길이를 입력해주세요(cm) : "))
    height = int(input("높이를 입력해주세요(cm) : "))
    
    trapazoid = ((upperWidth + lowerWidth) * height) // 2
    print(f"사다리꼴의 면적은 {trapazoid} cm2 입니다.")

def mainMenu() :
    sel = "0"
    while True :
        print("[1] 원의 면적 계산")
        print("[2] 사각형의 면적 계산")
        print("[3] 사다리꼴의 면적 계산")
        print("[0] 프로그램 종료")
        sel = input("메뉴를 선택해주세요 : ")
        
        if sel   == "1" :
            calCircle()
        elif sel == "2" :
            calQuadrangle()
        elif sel == "3" :
            calTrapezoid()
        elif sel == "0" :
            return
        else :
            print("오입력 되었습니다. 다시 선택해주세요.")

# elif 문을 줄이고 함수의 주소를 딕셔너리에 넣어서 메뉴를 호출함
# 리스트문으로도 구현 가능
def mainMenu2() :
    sel = "0"
    myfunctions = {"1" : calCircle , "2" : calQuadrangle , "3" : calTrapezoid}
    while True :
        print("[1] 원의 면적 계산")
        print("[2] 사각형의 면적 계산")
        print("[3] 사다리꼴의 면적 계산")
        print("[0] 프로그램 종료")
        sel = input("메뉴를 선택해주세요 : ")
        
        if sel in myfunctions.keys() :
            myfunctions[sel]()
        else :
            return

mainMenu2()
"""

"""
# 문제 [2]
# 리스트를 받아가서 리스트 안에 중복된 데이터를 제거하고 중복되지 않는 데이터 리스트만 반환하는 함수
list_1 = [1,2,3,4,5,6,7,8,4,5,6,7,8,9,10]

def listSet(list_1) :
    list_2 = list(set(list_1))
    
    return list_2

print(listSet(list_1))

# 문제 [3]
# myint 함수 생성 - 문자열을 받아가서 정수로 바꾸어서 반환하는 함수 생성
# "123" 을 넣었을 경우에는 123 을 반환하고, "123A" 등 잘못된 데이터를 입력하면 -1 을 반환
list_1 = ["1","2","3","4","A"]

def myInt(list_1) :
    for i in range(0,len(list_1)) :
        if ord(list_1[i]) < ord("0") or ord(list_1[i]) > ord("9") :
            return -1
    str = "".join(list_1)
    return int(str)

print(myInt(list_1))

# 문제 [4]
# 문장을 받아가서 문자열을 뒤집어서 보내는 함수
def reverse_2(str_1) :
    str_1 = list(str_1)
    str_2 = []
    for i in range(len(str_1)-1,-1,-1) :
        str_2.append(str_1[i])
    return str(str_2)

print(reverse_2("HELLO"))
"""

# 객체 지향 강의

# 클래스 ( 변수와 함수들의 집합 )
# 사용자가 정의하는 데이터 타입
# 객체를 만들기 위한 설계도 라고 볼 수 있음
# 클래스는 옛날부터 묵시적으로 대문자로 시작
# 파이썬은 클래스 안에서 변수 선언을 해서는 안됨(문제가 생길 가능성이 있음)

# 관련있는 데이터와 함수들의 집합
# 때로는 데이터만 존재하는 클래스도 있으며, 때로는 함수만 존재하는 클래스도 있음
# 대부분의 경우는 데이터와 함수가 같이 존재함
# 객체를 만들어야 비로소 메모리가 확보됨(원칙)
# 클래스는 데이터 타입이기에 메모리가 별도로 없음(원칙)

"""
class Person :
    name = "홍길동"         # name 이라는 클래스 변수
    age = 23               # age 이라는 클래스 변수
    # 해당 변수 영역은 객체를 만들때마다 호출되는 영역이 아니고 클래스 처음에 딱 한번 호출되는 영역
    # 따라서 이 영역 말고 변수는 생성자에서 만들어야 함
    # 객체가 생성될때마다 호출되는 함수
    # 객체가 생성될때마다 준비작업을 진행
    # 생성자의 호출자는 시스템임
    # 파이썬의 생성자는 __init__() 형태임 / 바꿀 수 없음
    # 생성자의 첫 번째 매개변수는 '무조건' self 임 - 객체 주소를 전달함
    # java 의 this 에 해당하는 요소가 self 임
    def __init__(self) :        # p1 = Person() 이라고 코드를 작성하였을 때 호출됨
        print("생성자 호출")

p1 = Person()              # 여기서의 p1 같은 것을 객체 또는 개체 라고 함
p2 = Person()
print(p1.name)
print(p1.age)

print(p2.name)
print(p2.age)
# 이 부분까지는 공통 변수 공간에서 확인하여 출력됨

# 이 때 비로소 메모리 공간이 확보되면서 만들어짐
p2.name = "임꺽정"
p2.age  = 75
print(p2.name)
print(p2.age)
"""
"""
class Person :
    # 이 공간은 클래스 공간으로 클래스 정의 시 딱 한번 실행됨(객체를 만들때마다 실행되는 공간이 아님)
    # 그래서 list 타입 또는 dict 타입 등을 여기서 선언 시 문제가 발생됨
    # 파이썬은 생성자에서 변수를 만들어야 함
    def __init__(self) :
        self.name  = ""
        self.age   = 0
        self.phone = []
    
    def append(self,name="임꺽정",age=13,phone="010-0000-0002") :
        self.name = name
        self.age = age
        self.phone.append(phone)
    
    def output(self) :
        print(self.name , self.age , self.phone)

p1 = Person()
p1.append("장길산",11,"010-0000-0003")

p2 = Person()
p2.append("홍금보",42,"010-0000-0004")

p1.output()
p2.output()
"""

"""
# 주급 : 이름 , 시간당 급여액 , 근무시간 -> 객체 지향으로 한사람 분만
class Person :
    def __init__(self , name = "" , paypertime = 0 , worktime = 0) :
        self.name       = name
        self.paypertime = paypertime
        self.worktime   = worktime
        self.calPay()
    
    def calPay(self) :
        self.totalpay = self.paypertime * self.worktime
    
    def outPut(self) :
        print("이름 : " , self.name , "\t시간당 급여액 : " , self.paypertime , "\t근무 시간 : " , self.worktime , "\t총 주급 : " , self.totalpay)

class Paymanager :
    
    def __init__(self) :
        self.person_list = [
            Person("홍길동" , 9700 , 20) ,
            Person("최길동" , 7700 , 25) ,
            Person("김길동" , 5700 , 15) ,
            Person("이길동" , 6500 , 35) ,
            Person("양길동" , 10700 , 10)
        ]
    
    def outPut(self) :
        for i in self.person_list :
            i.outPut()

mgr = Paymanager()
mgr.outPut()
"""

"""
class Book :
    def __init__(self , title = "" , price = 0) :
        print("self" , self)
        self.title = title
        self.price = price
        self.count = 10
        self.process()
    
    def process(self) :
        self.total_price = self.price * self.count
        
    def outPut(self) :
        print(self.title , self.price , self.total_price)

b1 = Book("채식주의자" , 500)
b1.outPut()
print(b1)
"""