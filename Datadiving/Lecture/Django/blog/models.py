from django.db import models

# Create your models here.

class BlogModel(models.Model) :
    title    = models.CharField("제목" , max_length = 200)
    contents = models.TextField("내용")
    writer   = models.CharField("작성자" , max_length = 50)
    wdate    = models.DateTimeField("작성일" , auto_now = True)
    hit      = models.IntegerField("조회수")

    def __str__(self) :
        return f"${self.title} ${self.writer}"