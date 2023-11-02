from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('exercise_library/', views.exercise_library, name='exercise_library'),
    path('create/', views.create_workout, name='create'),
]
