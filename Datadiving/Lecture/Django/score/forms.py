from django import forms
from .models import Score   # form 태그와 model 클래스 연동

class ScoreForm(forms.ModelForm) :
    # 내부 클래스
    class Meta :
        model = Score
        fields = ["name" , "kor" , "eng" , "mat"]
        labels = {
            "name" : "이름" ,
            "kor"  : "국어" ,
            "eng"  : "영어" ,
            "mat"  : "수학" ,
        }