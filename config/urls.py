"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# 08. import에 include를 추가한다. 이래야 하위 url 정보를 가져올 수 있다.

# 이대로 runserver를 하면 bmi/bmi_list.html이 없다는 에러가 뜬다.
# 이 때에는 먼저 templates 폴더를 만들고 그 하위에 bmi/bmi_list.html이 위치해ㅑㅇ 한다.
# >>> settings.py에 해당 내용이 있다.  APP_DIRS : True 이거 때문에

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bmi.urls')),
]
