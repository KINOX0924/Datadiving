from django.db import models

# Create your models here.
# 반드시 models.Model 을 상속받아야 함
# id 필드는 자동으로 만듬
# ORM = 객체 지향식 DB 접근을 하기 위함 - 쿼리를 만들지 않기 위함

class BlogModel(models.Model) :
    title    = models.CharField("제목" , max_length = 200)
    contents = models.TextField("내용")
    writer   = models.CharField("작성자" , max_length = 50)
    wdate    = models.DateTimeField("작성일" , auto_now = True)
    hit      = models.IntegerField("조회수")

    def __str__(self) :
        return f"${self.title} ${self.writer}"