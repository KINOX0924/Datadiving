# numpy = 분석용 라이브러리 , C 언어

import numpy as np

"""
# 넘파이 1

a = [1,2,3,4,5]
b = [2,4,6,8,10]

# 파이썬 코드
c = a + b
print(c)

# 넘파이 코드
# 타입을 list -> ndarray 타입으로 변경(C언어의 배열 , 속도가 매우 빠름)
# 머신러닝 , 딥러닝 둘 다 취급하는 데이터 타입이 ndarray 타입임
a1 = np.array(a)
print(a1 , type(a1))

b1 = np.array(b)
print(b1 , type(b1))

# 수학의 벡터연산을 수행함
# 스칼라연산 : 요소를 하나씩 더하기
# 벡터 연산  : 벡터 통째로(배열 통째로) 연산을 수행하여 for 반복문을 사용하지 않음
c1 = a1 + b1

print(c1)


x = np.array([1,2,3,4,5,6,7,8,9,10])

y = 2 * x + 3
print(y)

# 기초 통계
print("평균" , np.mean(x))
print("중위값" , np.median(x))
print("최소값" , np.min(x))
print("최대값" , np.max(x))
print("표준편차" , np.std(x))
print("분산" , np.var(x))
"""

"""
# 넘파이 2

# 수학적으로 아래와 같은 구조를 행,열(매트릭스) 라고 부름
m1 = np.array( [[1,2] , [3,4]])
m2 = np.array( [[5,6] , [7,8]])

m3 = m1 + m2
print(m3)

# 요소의 크기
print(m1.shape)         # 튜플 타입으로 반환
row , col = m1.shape    # 튜플
print(row , col)
print(m1.dtype)

for i in range(0 , row) :
    for j in range(0 , col) :
        print(m1[i][j] , end =" ")
    print()
"""

"""
# 넘파이 3

# range 함수 대신 arange(시작값 , 마지막값 , 증감치)
# for 나 list 필요 없음 , 자동으로 데이터 추출
print(np.arange(1,11))
print(np.arange(1,11,0.1))
print(np.arange(1,11,2))
print(np.arange(0,1,0.2))
print(np.arange(10,0,-1))

# 복사하기 - 얕은 복사
a = np.arange(1,11)

# 얕은 복사
b    = a
a[0] = 100

print(a)
print(b)

# 깊은 복사
c    = a.copy()
c[0] = -1

print(a)
print(c)

# 메모리 할당을 해서 요소의 값이 0 이나 1 로 채워진 ndarray 타입 만들기
a = np.zeros(10)
print(a)

b = np.zeros((3,4))
print(b)

c = np.zeros((3,4,2))
print(c)

d = np.ones((3,10))
print(d)

# 요소가 랜덤인 배열 또는 행렬 생성
# 평균 0 분산 1인 가우스분포(정규 분포) 를 따르는 난수를 발생
print(np.random.rand(10))
print(np.random.rand(2,3))
print(np.random.rand(2,3,4))

# 정수 발생 함수 np.random.randit(low , high , size) low ~ high 값을 size 만듬
print(np.random.randint(10,20,4))
print(np.random.randint(10,20,(2,3)))
"""

"""
# 넘파이 4

# 배열의 차원 변환
a = np.arange(10)
a = a.reshape(2,5)
print(a)
a = a.reshape(5,2)
print(a)

a = np.array([1,2,3,4,5])
b = np.array([2,4,6,8,10])

print( a + b )
print( a - b )
print( a * b )
print( a / b )

# 슬라이싱
x = np.arange(20)

print(x)
print(x[:10])   # 0 ~ 9번방
print(x[10:])   # 10번방 ~ 끝까지
print(x[::-1])  # 역순으로
print(x[10:2:-1])
print(x[10:0:-2])
print(x[1:3])
print(x[2:7])

# 조건식(넘파이 배열)
print( x >= 10 )
print(x[[1,3,5,7,9]])
print(x [x >= 10])


# 조건식(파이썬 리스트)
# 파이썬의 리스트는 조건식 적용 불가
# a = [1,2,3,4,5]
# print( a >= 3 )


# x 값이 짝수의 경우만
print(x[x % 2 == 0])

# 조건식 2
print(x[ np.logical_and(x % 3 == 0 , x % 5 == 0)])

# 조건식 3
x = np.array([1,2,3,4,5])
print(x[ [True , True, True , False , False]])

# 2차원의 슬라이싱
k  = np.array([[1,2,3,4,5] , [6,7,8,9,10] , [11,12,13,14,15] , [16,17,18,19,20]])
k2 = np.arange(20)
k2 = k2.reshape(4,5)

print(k)
print(k2)

# 전부다 출력
print(k[:])

# N 행만 출력
print(k[:1])
print(k[:2])
print(k[:3])

print(k[::2])
print(k[:2 , :2])
print(k[2:4 , 3:5])

# 넘파이 배열 합하기
a = np.array([1,2,3,4,5])
b = np.arange(6,11)

c = np.concatenate((a , b , np.arange(12,20)))
print(c)

# 배열 쪼개기
c1 = np.array_split(c , 3)
print(c1)

# where 검색
print(np.where(a % 2 ==0))

# 정렬
c1 = np.random.randint(1 , 100 , 10)    # np.random.randint(시작 , 끝 , 개체수)
print(c1)
c2 = np.sort(c1)
print(c2)
"""

"""
# 넘파이 5

# 랜덤값은 컴퓨터 내부의 시계를 이용해서 추출하는데 보고서를 쓸 때 값이 계속 바뀌면 문제가 되는 경우가 있음
# 그럴때는 seed 값을 사용

# **** argmax(가장 큰 값이 있는 위치값) , argmin(가장 작은 값이 있는 위치값) ****
np.random.seed(1234)    # seed 값은 0 부터 아무값이나 주면 됨
a = np.random.rand(5)
print(a)

# 기본적인 최댓값 , 최소값
print(np.max(a))
print(np.min(a))

print(np.argmax(a))
print(np.argmin(a))

# 문제 1. 가우스분포에 따른 랜덤값을 5개씩 10개 생성 , 각 행마다 제일 큰 값하고 큰 값의 위치를 찾아서 출력
np.random.seed(0)
arr = np.random.rand(10,5)
print(arr)

for row in arr :
    print(np.max(row) , np.argmax(row))
"""

"""
# 넘파이 6

# ndarray 를 파일로 저장하기 ***** 매우 중요함
data = np.random.rand(5)
print(data)

# 매트릭스는 중요하지 않지만 데이터는 한 개만 저장 가능함
# 파일명은 마음대로 설정 가능하지만 확장자는 변경 불가능
# (하나만) 저장
np.save("datafile.npy" , data)

# (하나만) 불러오기
data2 = np.load("datafile.npy")
print(data2)

# 여러개의 데이터 또는 이미지를 저장할 때 주로 npz 파일로 저장함
data3 = np.arange(1,11)
data4 = np.random.rand(10)
print(data3 , data4)

# 키와 값을 쌍으로 전달함(딕셔너리 타입)
# (여러개) 저장
np.savez("datafiles.npz" , key1 = data3 , key2 = data4)

# (여러개) 불러오기
file = np.load("datafiles.npz")
print(file["key1"])
print(file["key2"])
"""

# 넘파이 7
# linspace : 두 값 사이를 균등하게 나눔 , 그래프 좌표 등을 만들 때 주로 사용
# linspace(start , stop , num)  : 시작값 , 끝값 , 간격
a = np.linspace(1,10,50)
print(a)