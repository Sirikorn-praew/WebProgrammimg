from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('taskhome/', views.say_hello)
]