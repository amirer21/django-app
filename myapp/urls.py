from django.urls import path
from myapp import views

urlpatterns = [  
    path('', views.index), #home 접근했을때 views.py에 있는 함수 index로 위임
    path('create/', views.create), #create/로 접근
    path('read/<id>/', views.read) #read/1/로 접근 read/<id>/ <> 가변하는 값을 담을 수 있다
]
