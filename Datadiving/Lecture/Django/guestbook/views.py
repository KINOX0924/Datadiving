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