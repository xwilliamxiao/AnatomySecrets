from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('', views.WorkoutPlanList.as_view(), name='index'),
     path('exercise_library/', views.exercise_library, name='exercise_library'),
    #path('exercise_library/', views.ExercisesList.as_view(), name='exercise_library'),
    path('create/', views.create_workout, name='create'),
    #path('create/', views.UserCreatedExList.as_view(), name='create'),
]
