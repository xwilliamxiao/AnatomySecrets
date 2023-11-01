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

        #
        search_both_two = WorkoutPlan.objects.filter(days=workout_day, difficulty=workout_difficulty).distinct()

        return render(request, 'index.html',
                      {'workoutPlan': workoutPlan, 'exercises': exercises, 'search_both_two': search_both_two,})

    return render(request, 'index.html',
                  {'workoutPlan': workoutPlan, 'exercises': exercises})
