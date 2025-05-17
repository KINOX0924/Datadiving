# 파이썬의 입출력의 기본은 '파일 입출력'
# C 언어가 처음으로 모든 장비의 입출력 기본을 파일 입출력으로 한 이후 나온 언어들은 C 언어의 규칙을 따름
# 파일은 여러개가 있어서 특정 파일과 연결하는 작업이 필요하며 이를 open 이라고 함
# file = open("데이터파일.txt" , "w")
# 첫번째 파라미터는 경로를 포함한 파일명이며, 경로 생략 시 현재 프로그램이 가동중인 폴더에 파일을 생성
# 두번쨰 파라미터는 매개변수의 용도를 결정
# w 는 write 용으로 파일을 만들겠다는 의미
# 만일 파일이 없으면 새로 만들며 기존에 파일이 존재하면 내용을 모두 지움
# r 는 read 용으로 파일을 읽기만 하겠다는 의미
# 파일을 읽고 쓰고 나서는 닫고 다시 오픈을 해주어야함

# dir          = 파일 목록 확인
# dir *.확장자  = 해당 확장자의 파일만 목록 확인
# type 파일명   = 파일 내용 확인하기기

# 파일의 경로에 리눅스는 os / (슬래쉬) 를 사용
# 리눅스는 폴더나 파일에 공백이 안되며 , 대소문자를 구분 , 확장자는 구분하지 않음
# 파일의 경로에 윈도우는 os \ (역슬래쉬 , 한글폰트의 경우 원화표시) 를 사용
# 윈도우는 폴더나 파일에 공백 사용해도 됨 , 대소문자 구분하지 않음 , 확장자를 구분
# 따라서 바꾸고 싶으면 단계를 하나 거쳐서 진행 / TEST => 1 => test
# rstring 은 문자열 앞에 r 을 붙이면 escape 키(\) 를 무력화 시킴
# = r"c:\temp\test.txt"

# 파일읙 경로를 나타내는 방법
# 절대적 경로 : 루트(root) 부터 시작 (특별한 경우를 제외하고는 잘 사용하지 않음 / 폴더 전체가 이동될 때 문제 발생 가능성 큼)
# c:\temp\test.xtx
# 상대적 경로 : 현재 프로그램이 가동 중인 폴더를 기준으로 시작 (주로 사용)
# . : 내 폴더 / .. : 부모 폴더
# .\test.txt  = text.txt
# ..\text.txt = 현재 프로그램이 가동 중인 폴더보다 하나 위로 올라가서 파일을 생성
# 파이썬 공백있는 폴더명으로 들어갈때는 경로 전체의 앞/뒤에 " 를 붙혀주면 됨

# 드라이브명은 윈도우에만 있으며 리눅스에는 드라이브명이 없음
# 텍스트 파일 오류 발생 시 open 에 (encoding = "utf-8") 을 입력

# 반환 대상은 파일 객체
"""
file = open("데이터파일.txt" , "w")

# 출력이 파일로 감
file.write("Hello")
file.close()
"""

"""
f = open("데이터파일2.txt" , "w")
for i in range(1,11) :
    print(f"i = {i}" , file = f)
f.close()
print("작업 완료")
# print 함수의 기본 출력 장치가 모니터인데 file 이라는 파라미터에 file 객체를 주면 출력이 안되고 파일로 출력함

f2 = open("c:\\python folder\\데이터파일3.txt" , "w")
for i in range(1,11) :
    s = "i = %d" % (i)
    f2.writelines(s)
f2.close()
print("작업 완료")
"""

"""
# 파일을 읽기로 열때는 파일이 존재해야함
# read()      = 파일 전체를 통으로 읽음
f = open("데이터파일.txt" , "r")
data = f.read()

print(data)
print(type(data))
f.close

# readlines()   = 반환값이 리스트 타입 / 통으로 읽고 리스트로 가져옴
f = open("데이터파일.txt" , "r")
data = f.readlines()

print(data)
print(type(data))
f.close()

# readline()    = 반환값이 str 타입 / 한 줄만 딱 읽음
f = open("데이터파일.txt" , "r")
data = f.readline()

while data != "" :
    print(data)
    print(type(data))
    data = f.readline()
f.close()
"""

"""
f = open("데이터파일.txt" , "r")
data   = f.readline()
data_2 = 0
count  = 0

while data != "" :
    print("현재 데이터 값 : " , data)
    count  += 1
    data_2 += int(data)
    data    = f.readline()
f.close()

print("파일 내 숫자의 총 합 : " , data_2)
data_2 = data_2 // count
print("파일 내 숫자의 개 수 : " , count)
print("결과 : " , data_2)
print()

# =============

f = open("데이터파일.txt" , "r")
data = f.readlines()
sum  = 0

print(data)
for i in range(0,len(data)) :
    data[i] = data[i].strip().replace("\n"," ")
    sum += int(data[i])
f.close()

print(data)
avr = sum / len(data)
print(avr)
"""