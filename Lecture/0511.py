# 5월 11일 강의

# static 메서드 : 본래 메서드
# calss  메서드 : 

# 대부분의 클래스는 데이터와 함수의 결합
# 데이터는 없고 공통의 기능만 갖는 클래스를 만들수도 있음

# 사칙 연산을 하는 클래스
# 공통의 데이터 공간을 두고 설계할 수 있음

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

