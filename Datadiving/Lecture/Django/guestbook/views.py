from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

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
