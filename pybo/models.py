from django.db import models


# 모델 생성 및 변경시 >> $python manage.py makemigrations 로 sql 문 생성
# $python manage.py migrate 로 DB 업데이트 필수 !!
# 모델 사용 시에는 장고 셀을 이용 >> $python manage.py shell
# Create your models here.
class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

