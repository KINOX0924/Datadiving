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