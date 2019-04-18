
# 07. view를 만들고 난 뒤 사용자가 들어올 수 있도록 url을 지정해줘야 한다.
# 07-1. 먼저 urls.py를 만들고 아래의 내용을 타이핑
# 이건 맨날 쓰기 때문에 장고 프로젝트를 많이하면 파이참에 아얘 파일 명 별로 아래 내용이 자동으로 입력되도록 설정 가능하다.


from django.urls import path
from .views import *  # 10-4. 어차피 다 가져다 쓸테니 그냥 *로 바꾼다.

urlpatterns = [
    path("", BMIList.as_view(), name='index'),
    path("detail/<int:pk>/", BMIDetail.as_view(), name='detail'),
    path("delete/<int:pk>/", BMIDelete.as_view(), name='delete'),
    path("update/<int:pk>/", BMIUpdate.as_view(), name='update'),
    path("create/", BMICreate.as_view(), name='create'),
]