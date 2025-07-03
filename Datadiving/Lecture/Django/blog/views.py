from django.shortcuts import render
from django.http import HttpRequest , HttpResponse , JsonResponse
from .models import BlogModel as Blog
from django.core import serializers
# HttpRequest   : 클라이언트가 보낸 정보를 받아오는 객체
# HttpResponse  : 서버가 클라이언트로 보낼 정보를 저장해서 클라이언트에서 전달될 객체

# Create your views here.
# 웹에서 사람들이 정보를 요청하면 해당 페이지가 호출됨

# [1] - [1] 지금 이대로는 작동 불가 -> 이 함수와 url 을 연결하는 작업이 필요함
# http://127.0.0.1:8000/blog/list ==> blog/views.py 파일의 index 가 호출되게 해야함
# [2] config 의 urls.py 참고
# 매개변수에 request 가 반드시 있어야함
# [3] config/urls.py 과 guestbook/urls.py 참고

# [1]

def index(request) :
    return HttpResponse("Hello Django")

# 직렬화 : 객체를 파일이나 네트워크로 출력하고자 하는 걸 직렬화라고 함
def getList(request) :
    raw_data = list(Blog.objects.values())
    return JsonResponse(raw_data , safe = False , json_dumps_params = {"ensure_ascii" : False})
    