from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import WorkoutPlan, Exercises, UserCreatedEx
from django.views.decorators.http import require_POST
import requests


# Create your views here.
def index(request):
    workoutPlan = WorkoutPlan.objects.all()
    exercises = Exercises.objects.all()
    print("ACTIVATED")

    # Whenever the submit bottom is clicked
    if request.method == "POST":
        workout_day = request.POST.get('workoutDays')  # gets the radio button value
        workout_difficulty = request.POST.get('workoutDifficulty')

        # Filters the workout plans
        refine_plan = WorkoutPlan.objects.filter(days=workout_day, difficulty=workout_difficulty).distinct()

        return render(request, 'index.html',
                      {'workoutPlan': workoutPlan, 'exercises': exercises, 'refine_plan': refine_plan, })

    return render(request, 'index.html',
                  {'workoutPlan': workoutPlan, 'exercises': exercises})


def exercise_library(request):
    exercises_group = Exercises.objects.all().order_by('muscle_group')
    organized_data = {}
    for exercise in exercises_group:
        muscle_group = exercise.muscle_group
        if muscle_group not in organized_data:
            organized_data[muscle_group] = []
        organized_data[muscle_group].append(exercise)

    return render(request, 'exercise_library.html', {'organized_data': organized_data, })  # 'exercises':exercises

def create_workout(request):
    if request.method == "POST":
        new_name = request.POST.get('exercise_name')
        new_muscle_group = request.POST.get('muscle_group')
        new_description = request.POST.get('exercise_description')
        new_exercise = UserCreatedEx.objects.create(exercise_name=new_name, muscle_group=new_muscle_group, exercise_description=new_description)
        return redirect('create')
    user_exercise = UserCreatedEx.objects.all()
    return render(request, 'create.html', {'user_exercise':user_exercise})
