from django.shortcuts import render

# Create your views here.

# 06. CRUD-L
# create / read / update / delete LIST
# 함수형 뷰  - 제네릭뷰가 없는 case이거나 커스터마이징해서 사용하려고 할 경우에는 보통 이걸 쓴다. >> customizing이 class보다 쉽다.
# 클래스형 뷰 - 빈번하게 자주 사용되는 기능 또는 뷰는 제네릭 뷰가 이미 만들어져 있다. 이런걸 상속받아서 사용할 떄는 클래스형을 쓴다.


# 06 - 지난번에 함수형을 써봤으니 오늘은 클래스형
from django.views.generic.list import ListView
from .models import BMI

# generic view = model based view
class BMIList(ListView):
    model = BMI

# 10. 다른 뷰들도 만들어주자
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

# 10-1. 아래처럼 각각의 generic view들을 상속받는 형태로 만들어준다.
class BMIDetail(DetailView):
    model = BMI

class BMICreate(CreateView):
    model = BMI
    fields = ['weight','height']    # 10-2. create/update는 내용을 입력받아양 하므로 field를 지정해 준다.


class BMIDelete(DeleteView):
    model = BMI
    success_url = '/'               # 10-3. 각 동작을 성공하고난 뒤 어느 페이지로 이동할 것인지를 지정해 준다.

class BMIUpdate(UpdateView):
    model = BMI
    fields = ['weight', 'height']
    success_url = '/'