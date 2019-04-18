from django.db import models

# Create your models here.
# 어떤 데이터를 어떤 형태로 저장할 것인가?
# 모델은 class 형태로 작성한다.

# 01.
# models.Model : ORM 관련 기능(object relational mapping)을 이미 다 갖고 있다.
    # ORM : 실제 데이터를 코드로 추상화해놓고 사용한다.
        # ORM은 다른 언어나 프레임웤들도 지원하는데 형태는 각각 다를 수 있다. (클래스이거나 아니거나)
# 데이터를 저장/확인/수정/삭제 CRUD

class BMI(models.Model):  #models.Model을 상속받겠다.
    # 01.
    weight = models.FloatField()
    height = models.FloatField()
    bmi_score = models.FloatField(blank=True)  # 05. blank 지정
    created = models.DateTimeField(auto_now_add=True)  # 장고가 알아서 입력되는 해당 시간을 자동으로 넣어준다.

    # makemigrations bmi : 변경사항 추적, migration file을 만든다.
    # migrate bmi 001 : migration file을 실제 db에 반영


    # 03.
    def __str__(self):
        return "키 : "+ str(self.height)+"  체중 : "+ str(self.weight) + "  BMI : "+ str(self.bmi_score)

    # 04. data가 저장될 때 실행되는 magic method
    # bmi score를 계산해서 넣어주도록 처리한다.
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        self.bmi_score = self.weight / ((self.height/100)**2)


        super(BMI, self).save(force_insert, force_update, using, update_fields)