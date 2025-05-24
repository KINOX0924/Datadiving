# 05월 02일 강의

# 파이썬의 문자열은 Read Only
# s = "Life is too short, You need Python."
# print(s)

#                 # 인덱싱과 슬라이싱은 [0] 부터 시작
# print(s[:4])    # [0] 번부터 시작해서 3번까지만 출력 - 다른 프로그래밍 언어에서는 substring 이라는 함수로 슬라이싱을 지원함
# print(s[8:11])

#                 # 문자열의 인덱싱은 데이터 변환(수정) 이 불가능
# print(s[0])
# print(s[1])

#                                 # 문자열을 변경하고 싶을 때는 .replace() 를 사용
# s = s.replace("short" , "long") # 바꾼 데이터를 리턴하는데 이 때 바꾼 데이터를 받아야 함
# print(s)

# # 문자열 데이터량이 많을 때
# str_data =  """
# 홍길동,90,90,90
# 임꺽정,80,80,80
# 장길산,100,100,100
#             """

# lines = str_data.split("\n")
# print(lines)

# lines = lines[1:len(lines)-1]
# print(lines)

# name_list = []

# for line in lines :
#     words = line.split(".")
#     for i in words :
#         words_2 = i.split(",")
#         w = {"name" : words_2[0] , "kor" : words_2[1] , "eng" : words_2[2] , "math" : words_2[3]}
#         name_list.append(w)

# print(name_list)

# # 프린트 함수 포맷팅
# name = "홍길동"
# age = 23
# phone = "010-0000-0001"
# kor = 90
# eng = 90
# math = 90
# total = kor + eng + math
# avg = total // 3

# print("%s %d %s %d %d" %(name , age , phone , kor , eng))
# print("{} {} {} {} {}".format(name , age , phone , kor , eng))
# print(f"{name} {age} {phone} {kor} {eng}")      # 3.6 버전부터 사용 가능



# 배열 
# 프로그램 수행 전에 반드시 메모리를 확보해야함
# index 를 통해 읽고 씀
# 수행 도중에 크기 변화 불가
# 연속된 메모리 공간
# 인덱싱과 슬라이싱을 사용하여 접근한다는 부분만 배열구조와 일치

"""
list_1 = [1,2,3,4,5,6,7,8,9,10]
print(list_1)
print(list_1[1])
print(list_1[3])
print(list_1[5:10])
print(list_1[7])
print(list_1[9])

# 인덱스 데이터 추가
list_1.append(11)
list_1.append(12)
list_1.extend([13,14,15,16])
print(list_1)

list_1.clear()

list_1.insert(0,10)
list_1.insert(1,10)
print(list_1)
"""


# 강의 중 강사님 문제
# 리스트에 5 의 배수를 10 개 채우기
# 리스트에 100 부터 90 , 80 , 70 ... 역순으로 10 까지 채워서 출력하기
# 리스트에 1 ,2 , 3 , 2 , 4 , 3 , 5 , 1 이 있습니다. 중복을 제거하고 정렬된 리스트를 출력해보세요
# scores = [ 80, 95 , 70 , 100 , 85 ]  에서 평균 점수보다 높은 점수만 골라 새로운 리스트로 만들고 출력해보세요
# 집에 가서 다시 해보기



# 이차원 : 본래 의미의 배열이 아님
# list of list 로 표현해야 함
"""
a = [ [1,2,3] , [4,5,6] , [7,8,9] ]
for i in a :
    print(i)
"""

# 10 * 10 으로 100 개가 리스트에 들어가면 됨 , 처음에는 1 부터 100 까지 리스트 하나에 채워서 출력하기
"""
hund = []
list_1 = []

for i in range(1,101) :
    list_1.append(i)
    if i % 10 == 0 :
        hund.append(list(list_1))
        list_1.clear()
        
for i in range(0,len(hund)) :
    print(hund[i])

hund = []
hund_2 = []
count = 0
num = 0

for i in range(1,10) :
    count += 1
    for j in range(0,count) :
        num += 1
        hund.append(num)
    hund_2.append(list(hund))
    hund.clear()

print(hund_2)

for i in range(0,len(hund_2)) :
    print(hund_2[i])
"""

# 튜플은 요소값 삭제/수정 등이 불가능
# 함수 만들기 : 최대값과 최대값의 위치를 반환하는 함수
# a = [5,4,1,7,8,3,6]
# 첫번째 방의 데이터가 가장 크다고 가정 한다.
# 두번째 방의 데이터와 첫번째 방의 데이터를 비교한다.
"""
a = [5,4,1,7,8,3,6]

def getMax(list_1) :
    max = list_1[0]
    index = 0
    for i in range(1,len(list_1)) :
        if max < list_1[i] :
            max = list_1[i]
            index = i
    return max , index

print(getMax(a))

max , point = getMax(a)
print(max , point)

def add(x,y,z) :
    print("Call Me")
    return x*2 , y*2 , z*2

# 함수를 호출하면 변수에 받아 놓고 쓰자
a = add(3,4,5)
print(type(a))
print(a[0])
print(a[1])
print(a[2])
print(add(6,7,8)[0])
print(add(6,7,8)[1])
print(add(6,7,8)[2])
"""

"""
# 딕셔너리
person = dict()
person["name"]  = "홍길동"
person["age"]   = 23
person["phone"] = "010-0000-0001"

print(person)

person = {"name" : "장길산" , "age" : 41 , "phone" : "010-0000-0002"}
print(person)

# person dict 에서 키 값과 키 값의 밸류를 가져와서 출력
for key in person.keys() :
    print(key , person[key])

# person dict 에서 밸류 값만 출력
for value in person.values() :
    print(value)

# person dict 에서 아이템을 가져오고 키 값과 밸류 값을 튜플로 가져와서 출력
for key,value in person.items() :
    print(key , value)

# pserson dict 에서 가져온 키 값으로 index 와 value 값을 가져와서 출력
for key,value in enumerate(person.keys()) :
    print(key,value)
    
# 파이썬의 경우 연산자의 중복이 가능함
# 이 경우 완전히 새로운 데이터 타입을 만들거나 아니면 우리가 새로운 언어 번역기를 만들 때 필요함

mydic = {}
mydic["color"] = "색"
mydic["red"] = "빨간색"
mydic["green"] = "초록색"
mydic["blue"] = "파란색"
mydic["cyan"] = "청녹색"
mydic["black"] = "검정색"

color = input("알고싶은 색 :")

if color in mydic.keys() :
    print(mydic[color])
else :
    print("없는 색")
"""

# 집합 자료형
# 집합 자료형은 자동으로 중복 제거를 함
# 중복을 허용하지 않고 인덱싱을 허용하지 않음
"""
s1 = set([1,2,3,4,5,3,4])
print(s1)
print(type(s1))

s2 = list(s1)
print(type(s2) , s2)

# 집합 자료형 종류
s2 = set([3,4,6,7,9,7])
s3 = set([3,7,8,1,2,5])

# 교집합
s4 = s2.intersection(s3)
print(s4)

# 합집합
s4 = s2.union(s3)
print(s4)

# 차집합
s4 = s2.difference(s3)
print(s4)
"""