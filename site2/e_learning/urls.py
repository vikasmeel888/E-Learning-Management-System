"""e_learning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from elearning.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',home,name='home'),
    path('home/',home, name = "home"),
    path('login/',login, name='login'),
    path('inst_register/',inst_register,name='inst_register'),
    path('learner_register/',learner_register,name='learner_register'),
    path('buycourse/',buycourse,name = 'buycourse'),
    path('payment/<int:course_id>/',payment, name='payment'),
    path('bill/<int:course_id>/',bill,name = 'bill'),
    path('viewcourses/',viewcourses, name = 'viewcourses'),
    path('modifycourse/',modifycourse, name = 'modifycourse'),
    path('uploadcourses/',uploadcourses, name = 'uploadcourses'),
    path('freecourses/',freecourses, name = 'freecourses'),
    path('deletecourse/<int:course_id>',deletecourse, name = 'deletecourse'),
    path('bill/<int:course_id>',bill,name = 'bill')
]

