from django.db import models

# Create your models here.
# 반드시 models.Model 을 상속받아야함
# id 필드는 자동으로 만들어짐

# ORM - 객체지향식 DB 접근으로 쿼리를 만들기 쉬움
# 단 테이블이 너무 많고 Join 이 많거나 서브쿼리가 많을 때는 시간이 많이 걸리고 어려울 수 있음
# 테이블이 10 개 미만인 경우의 프로젝트 생성시 좋음

# Spring Entity 에 대응하는 것이 Model 클래스임
# 이 모델 기반의 테이블을 만들고 싶으면 setting.py 파일에 INSTALLED_APPS = [ 'blog.apps.BoardConfig' , ] 앱등록을 해주어야 함
# 파일 자체는 앱을 구축하면 자동으로 만들어줌

class BlogModel(models.Model) :
    title    = models.CharField("제목" , max_length = 200)
    contents = models.TextField("내용")
    writer   = models.CharField("작성자" , max_length = 50)
    wdate    = models.DateTimeField("작성일" , auto_now = True)
    hit      = models.IntegerField("조회수")

    def __str__(self) :
        return f"${self.title} ${self.writer}"
    
