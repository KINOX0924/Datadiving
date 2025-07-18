from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
# Create your views here.
# JsonResponse : dict 타입을 json 으로 바꾸어서 응답하는 클래스

def index(request) :
    return HttpResponse("guestbook")


# 파라미터 전달 방식
# [1] GET 방식 .1
# http://127.0.0.1:8000/guestbook/test1?x=5&y=7
# x=1&y=1 : 파라미터

# 데이터 전송 방식이 GET 방식일 경우에는 아래와 같이 작성하여 파라미터 값을 받음
# POST 전송 방식일 경우에는 POSTMAN 을 사용해야함
def test1(request) :
    x = request.GET.get("x")
    y = request.GET.get("y")
    return HttpResponse(int(x) + int(y))

# [2] GET 방식 .2
# http://127.0.0.1:8000/guestbook/test2/5/7
# 현재 권장 파라미터 전달 방식
def test2(request , x , y) :
    return HttpResponse(int(x) + int(y))

# [3] POST 방식
# http://127.0.0.1:8000/guestbook/test3
def test3(request) :
    if request.method == "POST" :
        x = request.POST.get("x")
        y = request.POST.get("y")
        return HttpResponse(int(x) + int(y))
    else :
        return HttpResponse("Error")
    
# 연습 문제 [1] : http://127.0.0.1:8000/guestbook/sigma/10
# 1 ~ 10 까지의 합계를 반환하기
def sigma(request , number) :
    sum_num    = 0
    
    for i in range(0 , int(number) + 1) :
        sum_num += i

    return HttpResponse(sum_num)
    
# 연습 문제 [2] : http://127.0.0.1:8000/guestbook/isLeap?year=2025
# 윤년 여부를 확인하여 반환값 출력
def isLeap(request) :
    year = request.GET.get("year")
    
    if int(year) % 4 == 0 and int(year) % 100 == 0 :
        return HttpResponse("윤년입니다.")
    else :
        return HttpResponse("윤년이 아닙니다.")

# 연습 문제 [3] : http://127.0.0.1:8000/guestbook/calc/add/4/5
# 연습 문제 [3] : http://127.0.0.1:8000/guestbook/calc/sub/4/5
# 더하기/빼기 연산 결과 반환하기
def calc(request , cals , a , b) :
    if cals == "add" :
        return HttpResponse(int(a) + int(b))
    elif cals == "sub" :
        return HttpResponse(int(a) - int(b))
    
# HTML 연동 작업
# HTML 페이지와 연동하고 싶으면 return render() 를 사용
# 앞의 Templates 를 생략해도 미리 settings 에 작성했기 때문에 기본적으로 Templates 에서 찾음
def list(request) :
    return render(request , "guestbook/guestbook_list.html" , {"title" : "HTML 연동하기" , "flowers" : flowers})

# 객체 출력
# DB 연동이 아직 안된 상태이니 list 로 데이터 전달
flowers = ["개나리" , "장미" , "찔레꽃" , "무궁화" , "백합" , "작약" , "국화" , "진달래" , "튤립" , "연꽃"]

# HTML 문서로 단순 이동 진행
def write(request) :
    return render(request , "guestbook/guestbook_write.html")

def save(request) :
    flower = request.POST.get("flower")
    return HttpResponse(flower)

# http://127.0.0.1:8000/guestbook/calwrite
# http://127.0.0.1:8000/guestbook/calsave

def calwrite(request) :
    return render(request , "guestbook/guestbook_addwrite.html")

def calsave(request) :
    x = request.POST.get("x")
    y = request.POST.get("y")
    opcode = request.POST.get("opcode")
    
    if opcode == "add" :
        return HttpResponse(f"{x} + {y} = {int(x) + int(y)}")
    elif opcode == "sub" :
        return HttpResponse(f"{x} - {y} = {int(x) - int(y)}")
    elif opcode == "mul" :
        return HttpResponse(f"{x} * {y} = {int(x) * int(y)}")
    elif opcode == "div" :
        return HttpResponse(f"{x} / {y} = {int(x) / int(y)}")
 
# 데이터를 주는 경우   
def getData(request) :
    return JsonResponse({"name" : "홍길동" , "age" : 23 , "phone" : "010-0000-0000"} , json_dumps_params={'ensure_ascii' : False})
# 한글 깨짐 문제 해결 : json_dumps_params={'ensure_ascii' : False}

def userinfo(request) :
    return render(request , "guestbook/userinfo.html")

# HttpResponse  - 그냥 텍스트로 응답할 때 - 실제 개발 , 연습용
# render        - html 문서와 파이썬 데이터를 하나로 묶어서 송신하면 새로운 html 문서를 만들어서 클라이언트로 반환함 (렌더링)
#               - 이러한 동작은 렌더링이라 함
# JsonResponse  - 데이터를 json 형태로 반환 , ui / ux (html 파트가 별도의 프레임워크로 만들어질 때 주로 사용)


# Django 가 DB 에 연돌하려면 보통 sqlite3 를 사용함(로컬에서만 사용)
# 단점 : 네트워크 지원을 하지 않음
# 따라서 MySQL 연동을 위해서는 mysqlclient 라이브러리가 필요함

"""
[1] mysql 연동
[2] Model 클래스를 만들어서 마이그레이션 테이블을 만드는 코드를 생성해야함
"""