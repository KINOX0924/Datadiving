from django.contrib import admin
from django.urls import path
from . import views

# [3]
# config/urls.py 파일이 모든 요청을 받아서 분배
# config/urls.py 파일 안에서 guestbook/urls.py 파일을 찾을 수 있게 해주어야함
urlpatterns = [
    path("" , views.index) ,
    path("test1" , views.test1) ,
    path("test2/<x>/<y>" , views.test2) ,
    # def text2(request , x , y) 에서의 매개변수의 명칭이 동일해야함
    path("test3" , views.test3) ,
    path("sigma/<number>" , views.sigma) ,
    path("isLeap" , views.isLeap) ,
    path("calc/<cals>/<a>/<b>" , views.calc) ,
    path("list" , views.list) , 
    path("write" , views.write) ,
    path("save" , views.save) ,
    path("calwrite" , views.calwrite) ,
    path("calsave" , views.calsave) ,
    
    # json 형식으로 응답
    path("getData" , views.getData) ,
    path("userinfo" , views.userinfo)
]