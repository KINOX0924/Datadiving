from django.db import models

# Create your models here.

# 프레임워크는 models.Model 을 무조건 상속받아야 함
# id 필드는 자동생성됨
class Score(models.Model) :
    name  = models.CharField("이름" , max_length = 40)
    kor   = models.IntegerField("국어")
    eng   = models.IntegerField("영어")
    mat   = models.IntegerField("수학")
    total = models.IntegerField("총점")
    avg   = models.FloatField("평균")
    wdate = models.DateField("작성일" , auto_created = True)
    

# 상기처럼 필드를 지정한 수 python manage.py makemigrations 을 수행하면 DB 에 만들 테이블을 파이썬 코드를 자동 생성