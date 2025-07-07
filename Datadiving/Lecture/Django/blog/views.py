from django.shortcuts import render
from django.http import HttpRequest , HttpResponse , JsonResponse
from .models import Blog
from django.core import serializers
from .forms import BlogForms
from django.utils import timezone
from django.shortcuts import redirect
# . = 나랑 같은 디렉터명 , forms = 파일명
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

# blog_write html 페이지로 이동만 함
def write(request) :
    return render(request , "blog_write.html")

def save(request) :
    form = BlogForms(request.POST)  # 여기서 직렬화가 이루어짐 , form.fieldList 에 있는 title 에 form 태그의 title 값이 차례대로 들어옴
    blogModel = form.save(commit = False)
    
    blogModel.wdate = timezone.now()
    blogModel.hit = 0
    blogModel.save()    # 확정
    
    # 보통 저장을 하고 나면 글목록으로 이동
    # 어떤 경우에도 직업 blog_list 메서드를 호출해서는 안됨
    # 글 등록 후에는 request 객체를 제거해야함(내용을 모두 비우고 정리 작업을 해야함)
    # 클라이언트로부터 다시 list 요청이 온 것처럼 해야함
    
    return redirect("blog:blog_list")