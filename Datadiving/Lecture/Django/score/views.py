from django.shortcuts import render , redirect
from django.utils import timezone
from django.http import HttpRequest , HttpResponse
from .models import Score
from .forms import ScoreForm

# Create your views here.

def index(request) :
    return redirect("score : score_list")

def list(request) :
    scoreList = Score.objects.all()
    return render(request , "score/score_list.html" , {"scoreList" : scoreList , "title" : "성적처리"})

def view(request , id) :
    return render(request , "score/score_view.html")

def write(request) :
    return render(request , "score/score_write.html")

def save(request) :
    if request.method == "POST" :
        # name = request.POST.get("name")
        scoreform  = ScoreForm(request.POST)
        scoreModel = scoreform.save(commit = False)
        # save 를 저장하는 시점에서 form -> model 로 전환되어 옴
        scoreModel.total = scoreModel.kor + scoreModel.eng + scoreModel.mat
        scoreModel.avg   = scoreModel.total/3
        scoreModel.wdate = timezone.now()
        scoreModel.save()
        # 프레임워크 단점 : 프로그래머의 의사를 많이 제한함
        # csrf : 정상적인 로그인을 납치해가서 다른 사이트에서 침입함
        # html 파일을 get 방식으로 부를 때 csrf_token 을 보내고 있음
        # restful API : html 없이 데이터만 주고 받을 수 있는 서버
    return redirect("score:score_list")