from django.contrib import admin

# Register your models here.

#02.

# 관리할 모델을 등록
# 관리자 페이지 커스터마이징

from .models import BMI

admin.site.register(BMI)