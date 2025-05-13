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