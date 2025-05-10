# ------------------------------------------------------------------------------------------------------------------------------------ #
# 강의 시작


# zip 함수
# 유일하게 파이썬에서만 제공해주는 함수

# 리스트가 2 개 이상 있을 때, 2 개의 리스트를 조합해서 새로운 형태로 만들고 싶을 때 사용
# a = [1,2,3,4,5]
# b = ["a","b","c","d","e"]
# == [("a,1"),("b,2"),("c,3"),("d,4"),("e,5")]

"""
a = [1,2,3,4,5]
b = ["a","b","c","d","e"]
for item in zip (a,b,a) :
    print(item)
    
ab_list = list(zip(a,b))
print(ab_list)
"""

# ------------------------------------------------------------------------------------------------------------------------------------ #
# 0429 에 작성했던 성적처리 코드 재활용 - 

# 외부 모듈(파이썬의 경우 파일) 을 이 메모리로 가져와서 결합(작업) 하라는 명령어
# random 이라는 함수는 정수 발생 함수
"""
import random

score_list = []

def init() :                # 맨 처음에 기본 데이터를 입력해놓고 시작하기 위한 함수
    names_list = ["홍길동" , "강감찬" , "곽재우" , "홍경래" , "서희" ,"윤관" , "김연아" , "안세영" , "조승연" , "장길산"]
    for i in range(0,10) :
        score_list.append({"name" : names_list[i] , "kor" : random.randint(20,100) , "eng" : random.randint(20,100) , "mth" : random.randint(20,100)})
    for s in score_list :
        s["sum"] = getSum(s)
        s["avg"] = getAvg(s)
        s["grade"] = getGrade(s)

def output(score_list) :
    for s in score_list :   # score_list 로부터 하나씩 s 라는 변수에 전달
        print(f"이름 : {s["name"]}",end="\t")
        print(f"국어 성적 : {s["kor"]}",end="\t")
        print(f"영어 성적 : {s["eng"]}",end="\t")
        print(f"수학 성적 : {s["mth"]}",end="\t")
        print(f"총 점 : {s["sum"]}",end="\t")
        print(f"평 균 : {s["avg"]:.0f}",end="\t")
        print(f"등 급 : {s["grade"]}")

def append() :
    s = {}
    
    s["name"]  = input("이름 입력 : ")
    s["kor"]   = getScore("국어")
    s["eng"]   = getScore("영어")
    s["mth"]   = getScore("수학")
    s["sum"]   = getSum(s)
    s["avg"]   = getAvg(s)
    s["grade"] = getGrade(s)
    
    score_list.append(s)
    
def getNumber(subject) :
    number = input(f"{subject} : ")
    while isDigit(number) == False :
        print("숫자만 입력해주세요.")
        number = input("정수를 입력하세요 : ")
    return int(number)

# input 으로 받는 모든 데이터는 string 타입
# ord 함수를 통해서 숫자인지 아닌지 판단 가능
# 문자열을 받아서 한글자씩 "0" 과 "9" 사이에 있는 지 확인
# 글자 중에 하나라도 0 - 9 사이에 존재하지 않으면 에러(숫자가 아닌 것으로 판단)
def isDigit(number) :
    for i in range(0,len(number)) :
        if ord(number[i]) < ord("0") or ord(number[i]) > ord("9") :
            return False
    
    return True

# 입력한 점수가 0 ~ 100 사이에 있는 숫자인지 확인
def getScore(subject = "국어" , limit = 100) :
    n = getNumber(subject)
    while n < 0 or n > limit :
        print(f"0 ~ {limit} 사이의 값을 입력하세요")
        n = getNumber(subject)
    return n

# 국어 , 영어 , 수학 성적 합산
def getSum(s) :
    return s["kor"] + s["eng"] + s["mth"]

# 합산 성적의 평균 계산
def getAvg(s) :
    return s["sum"] // 3

# 성적 평균에 따른 등급 설정
def getGrade(s) :
    if   s["avg"] >= 80 :
        return "수"
    elif s["avg"] >= 70 :
        return "우"
    elif s["avg"] >= 60 :
        return "미"
    elif s["avg"] >= 50 :
        return "양"
    else :
        return "가"

# filter 에서 두번째 파라미터 iterable (반복적인) 데이터를 전달 - list 류
# filter 안에서 list 안에서 한 개씩 객체를 가지고 옴
# 반환값이 list 타입이고 list 안에 dict 타입이 있음
# nameSearch 에서도 ouput() 함수를 출력하고 싶음
# 함수 안의 매개변수와 외부 전역변수의 이름이 동일하면 외부의 전역 변수보다 함수 안의 매개변수를 우선시함
def nameSearch() :
    name = input("검색하려는 이름을 입력해주세요 : ")
    result_list = list(filter(lambda x : x["name"] == name , score_list))
    
    output(result_list)
    
# 이름으로 검색하여 삭제 기능 추가
def nameDel() :
    name = input("삭제하려는 이름은 입력해주세요 : ")
    del_name = {}
    for i in filter(lambda x : x["name"] == name , score_list) :
        del_name = i
    score_list.remove(del_name)

# 이름으로 검색 후 수정 기능 추가
def nameModify() :
    name = input("수정하려는 정보의 이름을 입력하세요 : ")
    result_list = list(filter(lambda x : x["name"] == name , score_list))
    if len(result_list) == 0 :
        print(f"{name} 을 찾을 수 없습니다.")
        return
    
    # 두명 이상 있을 때의 처리 방법은 과제
    student = result_list[0]
    student["name"]  = input("수정할 이름을 입력해주세요 : ")
    student["kor"]   = getScore("국어")
    student["eng"]   = getScore("영어")
    student["mth"]   = getScore("수학")
    student["sum"]   = getSum(student)
    student["avg"]   = getAvg(student)
    student["grade"] = getGrade(student)
    print("입력한 정보로 수정되었습니다.")

def menuDisplay() :
    print("[1] 추가")
    print("[2] 출력")
    print("[3] 검색")
    print("[4] 삭제")
    print("[5] 수정")
    print("[0] 종료")
        
def start() :
    while True :
        menuDisplay()
        sel = input("메뉴 선택 : ")
        if sel   == "1" :
            append()
        elif sel == "2" :
            output(score_list)
        elif sel == "3" :
            nameSearch()
        elif sel == "4" :
            nameDel()
        elif sel == "5" :
            nameModify()
        elif sel == "0" :
            print("프로그램을 종료합니다.")
            return
        else :
            print("메뉴 입력을 잘못하셨습니다.")

init()         
start()
"""

# ------------------------------------------------------------------------------------------------------------------------------------ #

# 검색 알고리즘
# [1] 순차검색(선형검색)    : 데이터를 첫번째부터 순서대로 읽어서 해당 데이터를 찾을 때까지 또는 끝까지 가도 없으면 존재하지 않음 / 자료구조에서 실행 타임을 결정할 때 빅-O 표기법을 사용 "O(n)"
# [2] 색인순차             : 정렬해서 검색(추후 설명)
# [3] 이분검색             : 데이터가 반드시 정렬되어 있어야함 , 따라서 내부 데이터가 자주 바뀌면 정렬하는 시간이 더 오래 걸려서 항상 빠르다고 할 수 없음
#                         : 데이터를 절반으로 쪼개서 왼쪽을 선택할 지, 오른쪽을 선택할 지 선택하고 다시 선택한 부분을 절반으로 쪼개고 선택하고를 반복하여 검색함(원하는 데이터를 찾을 때까지)
#                         : 기본적으로 속도는 : O(logN)
# [4] 해쉬검색             : 이론상 검색 속도가 가장 빠름 , 속도를 위해서 만든 검색
#                         : 속도 때문에 메모리를 미친듯이 자치하며 구현도 어려움
# 과거에는 속도와 메모리 중 속도보다 메모리(가격) 를 우선시 했지만, 현재는 메모리보다는 속도를 중시함
# 파이썬은 dict 타입이 해쉬임 / dict = Dictionay = Hashmap = HashTable = Map
"""
a = [1,2,3,4,5,6,7,8,9,10]
key = 5         # 찾아야하는 값
find = -1       # bool 변수 / key 값을 못 찾은 상태


for i in range(0,len(a)) :
    if key == a[i] :
        print("found")
        find = i
        break
    
if find == -1 :
    print("not found")
else :
    print(f"{find} 번째에 있음")

def myFilter(a_list,key) :
    for i in range(0,len(a_list)) :
        if key == a[i] :
            return i
    return -1                   # for 문이 다 끝나고 key 값을 찾지 못함

pos = myFilter(a,4)
print(pos)

a = ["red" , "green" , "cyan" , "gray" , "blue"]
str = myFilter(a,"blue")
print(str)

a = [
    {"name" : "A" , "age" : 12},
    {"name" : "B" , "age" : 14},
    {"name" : "C" , "age" : 16},
    {"name" : "D" , "age" : 18},
    {"name" : "E" , "age" : 20}
     ]

dic = myFilter(a,{"name" : "A" , "age" : 12})
print(dic)

def myFilter2(key,a_list) :
    for i in range(0,len(a_list)) :
        if key(a_list[i]) :
            return i
    return -1

pos = myFilter2(lambda x  : x["name"] == "C" , a)
print(pos)
"""

# ------------------------------------------------------------------------------------------------------------------------------------ #

# 정렬       - 데이터베이스를 사용하는 순간 데이터베이스 쿼리에서 검색과 정렬을 지원
#           - 데이터베이스를 사용하지 못하는 상황에 파일을 써야한다면 직접 구현 필요
#           - 오름차순 정렬 = 올라가면서 정렬(작은 것부터 큰 것 순으로)
#           - 내림차순 정렬 = 내려가면서 정렬(큰 것부터 작은 것 순으로)
#           - select 정렬 / bubble 정렬 / quick 정렬(엄청 빠름/)

# select 정렬

"""
a_list = [5,3,2,4,1,8,7,10]

def selectSort(list) :
    b_list = [ s for s in list ]            # 하드 카피
    for i in range(0,len(b_list)-1) :
        for j in range(i+1,len(b_list)) :
            if b_list[i] > b_list[j] :
                b_list[i] , b_list[j] = b_list[j] , b_list[i]
    return b_list

b_list = selectSort(a_list)

print(a_list)
print(b_list)

b_list = sorted( a_list , key = lambda x : x , reverse = True)
print(a_list)
print(b_list)
"""

# sorted 함수를 직접 제작
"""
def mySorted(list , key , reverse = False) :
    modify_list = [ item for item in list ]
    if reverse == False :
        for i in range(0,len(modify_list)-1) :
            for j in range(i+1,len(modify_list)) :
                if key(modify_list[i]) > key(modify_list[j]) :
                    modify_list[i] , modify_list[j] = modify_list[j] , modify_list[i]
        return modify_list
    elif reverse == True :
        for i in range(0,len(modify_list)-1) :
            for j in range(i+1,len(modify_list)) :
                if key(modify_list[i]) < key(modify_list[j]) :
                    modify_list[i] , modify_list[j] = modify_list[j] , modify_list[i]
        return modify_list

a = [
    {"name" : "C" , "age" : 16},
    {"name" : "T" , "age" : 14},
    {"name" : "A" , "age" : 22},
    {"name" : "E" , "age" : 17},
    {"name" : "Z" , "age" : 20}
     ]

print(mySorted(a,lambda x : x["name"] , True))
print(mySorted(a,lambda x : x["age"]))
"""

# ------------------------------------------------------------------------------------------------------------------------------------ #

# 가변매개변수  : 함수의 매개변수 개수가 바뀌는 경우에 사용
#             : 변수 앞에 * 을 붙임(튜플 타입으로 함수에서 가져감)
#             : 매개변수에 기본값을 줄 때는 변수 자체가 여러 개 만들어짐

"""
def myadd(*args) :      # 변수 하나에 값을 여러개 전달 = 튜플 형태로 값을 전달하겠다는 의미
    print(type(args))
    for a in args :
        print(a)

myadd(1,2)
myadd(1,2,3)
"""

"""
def myadd2(*data) :
    s = 0 
    for i in data :
        s += i
    return s

print(myadd2(1,3,5))
print(myadd2(1,3,5,7))
print(myadd2(1,3,5,7,9))
"""
# 일반 매개변수(인자)와 튜플 매개변수(인자) 를 같이 혼용하여 사용해야 할 때는 일반 매개변수가 먼저 작성되어야 함 = 나머지 매개변수를 튜플로 받음
# 일반 매개변수와 튜플 매개변수와 dict 매개변수를 셋다 혼용하여 서용해야 할 때는 다음과 같은 순서로 작성 -> (일반인자 , 튜플인자 , dict 인자)
"""

def myadd3(n , *data) :
    print("n" , n)
    for i in data :
        print(i)

myadd3(1,2,3,4,5)   # 1 까지는 일반 매개변수로 받아지고 2 , 3 , 4 , 5 는 튜플 매개변수로 받아짐
"""

# dict 타입을 매개변수로 넘길수도 있음
# 이때는 매개변수의 전달 방식이 달라짐

# 함수 밖에서 dict 타입을 만들어서 함수로 매개변수로 넘겨주는 방식
"""
def myfunc(d) :
    print(d)

person = {"name" : "홍길동" , "age" : 12}
myfunc(person)
"""

# 함수 안에서는 key 값과 value 값만 매개변수로 넣어주고 함수 안에서 dict 타입으로 만들어서 출력
# 매개변수 앞에 ** 을 붙혀서 dict 타입으로 만들어지도록 함
"""
def myfunc2(**d) :
    print(d)

myfunc2(name = "홍길동" , age = 23)
"""

"""
def profile(role , *skills , **details) :
    print("role" , role)
    print("skills" , skills)
    print("details" , details)
    
profile("Programmer" , "Python" , "react" , "Deeplearning" , Salary = 100000000 , Position = "개발자")
"""

# ------------------------------------------------------------------------------------------------------------------------------------ #
# 04-30 과제

# 가위바위보 게임
# 컴퓨터가 1 , 2 , 3 중에 랜덤값 하나를 생각하고 있음
# 1 = 가위 , 2 = 바위 , 3 = 보
# 컴퓨터 승 , 사람 승 , 무승부
# 10 번을 해서 각 승률을 계산 / 컴퓨터 몇 번 , 사람 몇 번 , 무승부 몇 번 했는지 나오도록

# 여러 줄에 걸쳐서 문장을 작성할 때 \ 기호는 윗 문장과 아래 문장이 같은 줄이라는 의미(공백이 한 칸 필요)