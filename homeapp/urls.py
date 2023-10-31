from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_task', views.create_task, name='create a new task'),
    #first thing is the url, the second thing is function that it calls, third thing is just a name/description for youself
    #path('choose_plan', views.choose_plan, name='choose a plan'),
]
