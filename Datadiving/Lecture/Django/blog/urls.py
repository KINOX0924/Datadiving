from django.contrib import admin
from django.urls import path
from . import views

# [3]
# config/urls.py 파일이 모든 요청을 받아서 분배
# config/urls.py 파일 안에서 guestbook/urls.py 파일을 찾을 수 있게 해주어야함
urlpatterns = [
    path("",views.index)
]