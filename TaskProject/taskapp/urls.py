from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('', views.login_user, name='login'),
    path('taskapp/', views.taskView, name='taskapp'),
    path('logout/', views.log_user_out, name='logout')
    # path('addTask/', views.addTask), 
]