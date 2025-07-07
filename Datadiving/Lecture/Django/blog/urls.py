from django.contrib import admin
from django.urls import path
from . import views

# [3]
# config/urls.py 파일이 모든 요청을 받아서 분배
# config/urls.py 파일 안에서 guestbook/urls.py 파일을 찾을 수 있게 해주어야함

app_name = "blog"
urlpatterns = [
    path("",views.index) ,
    path("list/" , views.getList , name = "blog_list") ,
    path("write/" , views.write , name = "blog_write") ,  # html 페이지로 이동
    path("save/" , views.save , name = "blog_save") ,     # 데이터를 받아서 DB 에 저장
]