"""
# mod1 에 있는 모듈을 사용
# 파일 전체가 메모리에 로딩됨
import mod1

if __name__ == "__main__" :
    print(mod1.add(3,4))
    print(mod1.sub(3,4))

    p2 = mod1.Person("최번개" , 7)
    p2.print()
    
# 에일리어싱(aliasing)
# 모듈 이름이 너무 길때 다른 이름으로 변경하여 사용하는 것
import mod1 as md

print(md.add(5,6))
print(md.sub(5,6))

p3 = md.Person("노진구" , 9)
p3.print()

# 모듈명도 쓰기 싫고 마치 내 함수처럼 사용하고 싶을 때는 from 모듈명 import 함수명
# 대신 불러온 함수를 제외하고는 사용할 수 없음
from mod1 import add , sub
print(add(9,8))
print(sub(9,8))

from mod1 import Person
p4 = Person("퉁퉁이" , 9)
p4.print()


# numpy
# numpy 모듈을 사용하여 벡터 연산이 가능함

# 스칼라 연산 = 1 : 1 연산 / 대부분의 프로그래밍 언어가 해당 연산을 지원
# 백터 연산   = 다 : 다 연산 / 통계 분석용 언더들은 수학에 가깝게 벡터 연산을 지원
# : 대표적으로 R 언어 , 파이썬(자체는 제외) 의 numpy , pandas 라이브러리
import numpy as np
a = [1,2,3,4,5,6,7,8,9,10]
b = [x**2 for x in a]
c = a + b
print(a)
print(b)
print(c)

a1 = np.array(a)
b1 = 2 ** a1
c1 = a1 + b1
print(a1)
print(b1)
print(c1)
"""

"""
import mod1 as md1

print(md1.isEven(22))
print(md1.isEven(21))

print(ord("a"))
print(ord("A"))
print(ord("b"))
print(ord("B"))
print(md1.toUpper('asterisk'))
"""