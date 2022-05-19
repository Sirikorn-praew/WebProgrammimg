from django.urls import path
from . import views

#URLConf
urlpatterns = [
    # path('', views.login_user, name= 'login'),
    path('taskhome/', views.taskView, name= 'tasks'),
    # path('addTask/', views.addTask), 
]