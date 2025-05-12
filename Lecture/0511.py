# 5월 11일 강의

# static 메서드 : 본래 메서드
# calss  메서드 : 

# 대부분의 클래스는 데이터와 함수의 결합
# 데이터는 없고 공통의 기능만 갖는 클래스를 만들수도 있음

# 사칙 연산을 하는 클래스
# 공통의 데이터 공간을 두고 설계할 수 있음

"""
class Calculator : 
    def __init__(self , x = 0 , y = 0) :
        self.x = x
        self.y = y
    
    def add(self) :
        return self.x + self.y
    
    def sub(self) :
        return self.x - self.y
    
class Calculator2 :
    def add(self , x , y) :
        return x + y
    
    def sub(self , x , y) :
        return x - y

c1 = Calculator(4,5)
print(c1.add())
print(c1.sub())

c2 = Calculator2()
print(c2.add(9,8))
print(c2.sub(9,8))


# static 메서드
# JAVA 는 어노테이션이라고 함
# 장점 : 객체하고는 관계없이 사용 가능 / self 를 매개변수도 가질 수 없음 / 사용이 간편함
# 사용목적 : 객체를 만들지 않고 특정 메소드를 사용하고 싶을 때 사용

# DB 에 접근해야하는 클래스를 만들때 코드를 각각의 클래스가 소유할 경우 문제점
# [1] DB 의 IP , ID , PASSWORD 가 바뀌었을 때 모든 클래스에서 수정을 해야 , 패스워드가 드러나게 하면 안됨
# = static 메서드나 classmethod 로 구성된 클래스를 만들어서 사용하는 것이 바람직함
# [2] 프로그램이 너저분해짐

# static 메서드는 클래스 변수를 건드릴 수 없기에 classmethod 를 사용함


# static 메서드 : 함수들간의 기능적 유기성은 있지만 데이터(DB) 는 필요하지 않을 때 사용
# class 메서드  : 매개변수 cls 를 갖고 다니며 class 변수에 접근가능
class Calculator3 :
    @staticmethod
    def add(x , y) :
        return x + y
    
    @staticmethod
    def sub(x , y) :
        return x - y

c3 = Calculator3()
print(c3.add(9,8))
print(c3.sub(9,8))

print(Calculator3.add(4,5))
print(Calculator3.sub(4,5))

class Calculator4 :
    @classmethod
    def add(cls , x , y) :
        return x + y

    @classmethod
    def mul(cls , x , y) :
        return x * y

print(Calculator4.mul(5,5))

"""

"""
class MyClass :
    # 클래스 변수의 영억
    # 객체의 생성과는 상관없이 한 번만 만듦
    # 생성자에서 이 부분을 건드리면 안됨
    
    count = 0
    # 목적 : 객체가 만들어질때마다 몇 개 만들어졌는 지 확인하고 싶음
    
    @staticmethod
    def addCount() :
        count += 1
    # 스테틱 메서드 입장에서는 매개변수(self) 를 사용할 수 없으니깐 클래스 변수인 count 변수에 접근 불가
    
    @classmethod
    def plusCount(cls) :
        cls.count += 1
        return 
    # (cls) 가 '클래스' 를 의미함

MyClass.plusCount()
print(MyClass.count)
"""

# 객체를 만들 때 객체의 개수를 카운트 하거나 제한하는 클래스를 만들고자 할 때 classmethod 를 사용

"""
class SelfCount :
    # 변수에 __ 를 붙이면 외부에서 접근이 불가능함
    # 기본적으로 파이썬의 변수는 모두 퍼블릭(공개) 변수인데 변수의 앞에 __ 를 붙히면 프라이빗(비공개) 성질을 가짐
    __count = 0     # 클래스 변수 선언
    
    def __init__(self) :
        SelfCount.__count += 1
    
    @classmethod
    def printCount(cls) :
        print(cls.__count)

# __count 변수가 프라이빗이기 때문에 외부에서 호출이 불가능함
# print(SelfCount.__count)
s = SelfCount()
SelfCount.printCount()
s = SelfCount()
SelfCount.printCount()
s = SelfCount()
SelfCount.printCount()
s = SelfCount()
SelfCount.printCount()
s = SelfCount()
SelfCount.printCount()
"""

# 객체를 하나만 만들 수 있는 클래스 = 싱글톤 패턴
# 왜(?) 객체를 하나만 만들어야 할까

# DB 커넥션풀(DB 를 읽고 사용하고 나가고, 읽고 사용하고 나가고 등을 반복하는 풀) 을 만들어 사용할 때 DB 가 연결-사용-끊기를 반복함
# 근데 이 때 사용시간 보다 연결 - 끊기 시간이 더 많은 시간을 소요
# 따라서 미리 연결자를 많이 만들어두고 연결자를 돌려가며 사용 - 풀 기법
# 이 풀은 객체 하나만 만들게 해야 하는데 이를 두고 싱글톤 패턴이라고 함
class Singleton :
    # 객체를 하나만 만들어야 함
    __instance = None   # 객체를 만들라고 하면 None 이 아닐때만 객체를 만들고 None 이면 있던 객체를 반환함
    
    @classmethod
    def getInstance(cls) :
        if cls.__instance == None :
            cls.__instance = cls.__new__(cls)
        # 클래스를 이용해서 인스턴스를 만드는 방법
        return cls.__instance
    
    def display(self) :
        print("************")
        
    def __init__(self) :
        # 이미 객체가 존재하면 강제로 에러를 발생시킴
        if Singleton.__instance is not None :
            raise Exception("이 클래스는 반드시 getInstance 로만 객체 생성이 가능합니다")

s = Singleton.getInstance()
s.display()

s2 = Singleton.getInstance()
s2.display()

# 파이썬에서는 클래스 외부에서 객체를 만드는 것을 파이썬이 막을 방법이 없음
# 다른 언어들은 생성자한테도 접근권한이 있어서 이걸 private 로 만들면 외부에서 객체 생성을 못 함
# 파이썬 생성자에 이미 __ 붙어있어서 별도로 접근 권한을 건드릴 수 없음 = 그래서 편법을 사용해야함

# 데이터 없이 일을 하는 클래스들을 만들때는 쓰레드풀로 만들면 좋다
# 쓸데없이 객체가 만들어졌다 없어졌다를 하는 것을 방지할 수 있음