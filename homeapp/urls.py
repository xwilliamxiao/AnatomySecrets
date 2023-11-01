from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #first thing is the url, the second thing is function that it calls, third thing is just a name/description for youself
    #path('choose_plan', views.choose_plan, name='choose a plan'),
]
