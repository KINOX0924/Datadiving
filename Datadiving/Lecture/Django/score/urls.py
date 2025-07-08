from django.contrib import admin
from django.urls import path
from . import views

app_name = "score"
urlpatterns = [
    path("",views.index) ,
    path("list" , views.list , name = "score_list") ,
    path("view/<id>" , views.view , name = "score_view") ,
    path("write" , views.write , name = "score_write") ,  # html 페이지로 이동
    path("save" , views.save , name = "score_save") ,     # 데이터를 받아서 DB 에 저장
]