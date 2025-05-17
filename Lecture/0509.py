# 학생 명단 데이터파일을 받아서 나누기
"""
student_list = []
name_list = ["이름 : " , "국어 : " , "수학 : " , "영어 : " , "총점 : " , "평균 : " , "등급 : "]

f = open("데이터파일.txt" , "r" , encoding = "UTF-8")
data = f.readline()

while data != "" :
    itemlist = []
    data = data.strip().replace("\n" , " ")
    itemlist = data.split(",")
    student_list.append(itemlist)
    print(itemlist)
    data = f.readline()

f.close()

for i in range(0,len(student_list)) :
    sum = 0
    avr = 0
    length = 0
    for j in range(0,len(student_list[i])) :
        if j >= 1 :
            sum += int(student_list[i][j])
            
    student_list[i].append(sum)
    student_list[i].append(sum//3)
    length = len(student_list[i]) - 1
    
    if student_list[i][length] >= 90 :
        student_list[i].append("A")
    elif student_list[i][length] >= 80 :
        student_list[i].append("B")
    elif student_list[i][length] >= 70 :
        student_list[i].append("C")
    elif student_list[i][length] >= 80 :
        student_list[i].append("D")
    else :
        student_list[i].append("F")

for i in range(0,len(student_list)) :
    for j in range(0,len(student_list[i])) :
        print(f"{name_list[j]} {student_list[i][j]}" , end = "\t")
    print()
"""

"""
list_2 = []
list_3 = [0,0,0,0,0]
dict_1 = {"sepal length(cm)" : 0 , "sepal width (cm)" : 0 , "petal length (cm)" : 0 , "petal width (cm)" : 0 , "target" : 0}
count  = 0

f = open("iris.csv" , "r")
data   = f.readline()

while data != "" :
    list_1 = []
    
    data   = data.strip().replace("\n" , " ")
    list_1 = data.split(",")
    
    if count >= 1 :
        for i in range(0,len(list_1)) :
            list_3[i] += float(list_1[i])
    
    list_2.append(list_1)
    count += 1
    data   = f.readline()
    
f.close()

for i in range(0,len(list_3)) :
    list_3[i] = list_3[i] / (len(list_2) - 1)
print(list_3)

count = 0
for key in dict_1 :
    dict_1[key] = list_3[count]
    count += 1

print(dict_1)
"""

"""
lst_1  = []
dict_1 = {"3" : 0 , "4" : 0 , "5" : 0 , "6" : 0 , "8" : 0}

# 실린더 개수 카운트 : 3 , 4 , 5 , 6 , 8

f    = open("mpg.csv" , "r")
data = f.readline()

while data != "" :
    data = data.strip().replace("\n" , " ")
    lst_1.append(data.split(","))
    
    data = f.readline()
f.close()

for i in range(1,len(lst_1)) :
    if lst_1[i][1] in dict_1.keys() :
        dict_1[lst_1[i][1]] += 1

print(dict_1)
"""

# with
# 파이썬 버전이 낮을 경우 거듭해서 파일을 오픈하면 에러가 발생됨
# 그냥 open 을 바로바로 사용하는 것은 위험한 방식이기에 거듭해서 파일을 오픈해야 할 필요가 있는 경우에는 with 구문을 사용할 것
"""
with open("mpg.csv" , "r") as f :
    lines = f.readlines()
    print(lines)
"""

# pickle 함수
# 직렬화    : 생성한 객체 자체를 파일이나 네트워크로 메모리 그대로 저장하는 것을 말함(바이너리 형태/2진수 파일)
# 역직렬화  : 파일이나 네트워크로부터 객체를 읽어들임
# 단 pickle 로 저장한 것은 pickle 밖에 읽을 수 없음

import pickle

# 직렬화    / "wb"
data = {"name" : "홍길동" , "age" : 30 , "phone" : "010-1000-1000"}
with open("data.bin" , "wb") as f :
    pickle.dump(data , f)

# 역직렬화  / "rb"
with open("data.bin" , "rb") as f :
    data2 = pickle.load(f)

print(data2)