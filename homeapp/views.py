from django.shortcuts import render
from django.http import HttpResponse
from .models import WorkoutPlan, Exercises
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
    # Load in all the exercises
    # exercises = Exercises.objects.all()

    # Testing to see if I can print the muscle_group and then the
    exercises_group = Exercises.objects.all().order_by('muscle_group')
    organized_data = {}
    for exercise in exercises_group:
        muscle_group = exercise.muscle_group
        if muscle_group not in organized_data:
            organized_data[muscle_group] = []
        organized_data[muscle_group].append(exercise)

    return render(request, 'exercise_library.html', {'organized_data': organized_data, })  # 'exercises':exercises
