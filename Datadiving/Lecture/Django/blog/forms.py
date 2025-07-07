from django import forms
from blog.models import Blog

class BlogForms(forms.ModelForm) :
    # Meta class : 클래스 안에 별도의 클래스를 만드는 것
    class Meta :
        model = Blog
        fields = ["title" , "writer" , "contents"]
        labels = {
            "title" : "제목" ,
            "writer" : "작성자" ,
            "contests" : "내용"
        }