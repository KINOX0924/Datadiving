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
    num     = request.GET.get("number")
    sum_num    = 0
    
    for i in range(0 , int(num) + 1) :
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