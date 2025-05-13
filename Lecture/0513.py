# 5월 13일 강의

# 클래스의 상속
# 다른 언어의 경우는 부모 생성자를 먼저 호출하고 자식 생성자를 호출하지만 파이썬은 다름
# 상속을 사용하는 이유 : 처음부터 만들려고 하면 힘드니깐 기본은 만들어두고 상속받은 클래스를 기반으로 양식에 맞게 변경하여 개발하는 것

"""
# 부모 클래스
class Base :
    def __init__(self , x = 0 , y = 0) :
        self. x = x
        self. y = y
        print("Base 생성자")
    
    def display(self) :
        print(f"x = {self.x} , y = {self.y}")
    
    def add(self) :
        return self.x + self.y
    
    def doubleX(self) :
        return self.x * 2
    
    def doubleY(self) :
        return self.y * 2


class Child1(Base) :
    def __init__(self , x = 0 , y = 0 , z = 0) :
        # 부모 클래스의 부모 생성자에서 하는 일(코드) 가 굉장히 많은 경우 부모생성자를 호출하는 방식으로 설계하는 것이 바람직함
        # super() 함수는 부모 생성자를 호출하는 코드
        # : 부모 클래스의 함수를 먼저 호출하고 내가 만든 코드를 붙이고자 할 때 사용
        super().__init__(x,y)
        self.z = z
        print("Child1 생성자")
        
    # 다형성 : 오버로딩 / 오버라이딩
    # 오버로딩(OverLoading)
    # : 동일 클래스 내에서 함수의 이름이 같지만 형태가 다른 함수(매개변수의 타입이나 개수를 달리함)
    # : 파이썬은 오버로딩은 미허용하지만 기본값을 줌으로서 유사한 결과를 가져올 수 있음
    
    # 오버라이딩(OverRiding)
    # : 부모 클래스와 자식 클래스 간에 이루어지는 기능이며 부모 클래스에 있는 메서드가 마음에 들지 않아 고쳐쓰고 싶을 때
    # : 부모 클래스의 함수 이름과 자식 클래스의 함수 이름이 같으면 부모의 함수를 가려버리고 자식 클래스 내의 함수를 사용함
    def display(self) :
        print(f"x = {self.x} , y = {self.y} , z = {self.z}")

p = Base()
p.display()

p = Base(5,4)
p.display()

c1 = Child1(2,3,4)
c1.display()
print(c1.doubleX())
"""

# 중첩 상속
# A 클래스의 기능을 B 클래스가 상속받고 B 클래스의 기능을 C 클래스가 상속받는 경우

# 다중 상속
# 파이썬은 기본적으로 다중 상속을 허용 (자바는 허용하지 않음)
# : 클래스를 동시에 여러개 상속 받는 경우를 말함
# : A 클래스가 B 클래스의 기능을 한 번에 C 클래스가 상속받는 경우

# 다중 상속에서 각 부모 클래스에서 동일명의 함수가 존재하는 경우 먼저 매개변수로 선언된 클래스의 메서드(함수) 를 호출하여 사용
"""
class Flyable :
    def fly(self) :
        print("날 수 있다")
    
    def walk(self) :
        print("두 다리로 걷는다")

class Swimmable :
    def swim(self) :
        print("수영할 수 있다")
        
    def walk(self) :
        print("***두 다리로 걷는다***")
        
class Duck(Swimmable , Flyable) :
    def quack(self) :
        print("꽥꽥")

d1 = Duck()
d1.fly()
d1.swim()
d1.quack()
d1.walk()


# 시스템이 제공하는 내장 변수 중에 __mro__ : 클래스 상속을 받는 관계정보(순서(우선도)) 를 말해줌
# 자식 클래스.__mro__
print(Duck.__mro__)
"""

# 다이아몬드 상속
# super() 를 사용하지 않으면 이전 버전의 파이썬에서 문제가 발생할 수 있기에 super() 만 사용 필요
"""
class A :
    def __init__(self) :
        print("A 생성자 호출")

class B(A) :
    def __init__(self) :
        print("B 생성자 호출")
        super().__init__()

class C(A) :
    def __init__(self) :
        print("C 생성자 호출")
        super().__init__()
        
class D(B,C) :
    def __init__(self) :
        print("D 생성자 호출")
        super().__init__()

d = D()
print(d)
print(D.__mro__)
"""

# isinstance(객체 , 클래스) 함수
# 이 객체가 클래스의 인스턴스(객체) 인지 확인해주는 함수
# object 라는 객체는 모든 클래스의 Base 클래스이기에 무조건 상속을 받는 클래스
"""
print(isinstance(d,A))
print(isinstance(d,B))
print(isinstance(d,C))
print(isinstance(d,D))
print(isinstance(d,object))
print(isinstance(d,str))
print(isinstance(d,int))
"""

# 예외처리 try
# except 구역은 에러ㅏ 발생 시 실행되는 코드 / error 부분에는 에러 구문이 저장됨
# finally 구역은 에러가 발생하든 않든 반드시 실행되어야 하는 코드를 작성 / 파일 처리 , 데이터베이스 , 네트워크 처리 등에 사용됨
# : 왜냐하면 파일 , 데이터베이스 , 네트워크는 연결 도중 오류가 발생 시 close 가 실행되어야 하는데 이 close 를 finally 에 넣어줌
"""
try :
    x = int(input("정수 : "))
    y = int(input("정수 : "))

    z = x / y
    print(f'x = {x} , y = {y} , z = {z}')
except ZeroDivisionError as error :
    print("0 으로는 숫자를 나눌 수 없습니다.")
finally :
    print("이 부분은 반드시 실행된다.")
"""

"""
try :
    f = open("file1.txt" , "r")
    lines = f.readlines()
    
    for line in lines :
        print(line)
except FileNotFoundError as Error :
    print(Error)
except NameError as Error :
    print(Error)
except Exception as Error :
    print(Error)
finally :
    f.close()
"""

"""
# 폭포수(케스케이드 기법)
try :
    a = [1,2,3,4,5]
    b = a[5]
except ZeroDivisionError as Error :
    print(Error)
except IndexError as Error :
    print(Error)
except Exception as Error :
    print(Error)
"""

# raise
# 강제 예외 발생 코드
# 원래 함수 종료 구문은 return
# return 이 하는 일 : 값 반환 , 함수가 끝날 때 마무리 작업
# return 이 명시되어 있지 않을 때(생성자에 주로 return 대신 raise 를 사용) / raise 가 함수의 정리도 진행함

"""
class Test :
    def __init__(self) :
        raise Exception("객체 생성 오류")

try :
    t1 = Test()
except Exception as Error :
    print(Error)


print(dir(Test))
print(divmod(98,9))

result = eval('1+2+3')
print(result)

result = eval('(4+3) * (55-61)')
print(result)
"""

"""
a = [1,4,-2, 5,-5,8,-6,7,0]
po_lsit = []

def isPositive(x) :
    if x > 0 :
        return True
    return False

po_lsit = list(filter(lambda x : x > 0 , a))
print(po_lsit)
"""

"""
# 말일까지 남은 날짜 구하기
import datetime
day1 = datetime.date(2021,12,14)
day2 = datetime.date(2024,7,25)

calDay = day2 - day1    # timedelta 객체로 바뀌고 날짜를 가지고 있음
print(day1)
print(day2)
print(calDay.days)

import calendar
from datetime import date

today = date.today()
year  = today.year
month = today.month

last_day = calendar.monthrange(year , month)[1]

print(last_day)

day1 = datetime.date(year , month , last_day)
print((day1 - today).days)

# 오늘이 무슨 요일 인지 확인
print(today.weekday())
"""

"""
# 날짜를 입력을 받아서 그 날이 무슨 요일인지 반환하는 함수
# 문자열로 입력 받을 것 : "2025-05-11"
import datetime

def whatDay(date) :
    day_list = ["월요일" , "화요일" , "수요일" , "목요일" , "금요일" , "토요일" , "일요일"]
    now_day = datetime.datetime.strptime(date , '%Y-%m-%d')
    
    day_index = now_day.weekday()
    
    return day_list[day_index]

today = '2025-05-13'
print(whatDay(today))
"""

# 딥러닝 때 shutil 을 주로 사용함
import shutil

shutil.copy("0513.py" , "0515.py")