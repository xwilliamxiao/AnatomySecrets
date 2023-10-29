from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import WorkoutPlan, Exercises
import requests



# Create your views here.
def index(request):
    # Global variables
    selected = False
    print(selected)
    workoutPlan = WorkoutPlan.objects.all()
    exercises = Exercises.objects.all()
    print("ACTIVATED")

    # --- WORKOUT PLAN ---
    workout_plan = WorkoutPlan.objects.get(pk=4) #The primary key
    exercise_test = workout_plan.exercises.all()

    for exercise in exercise_test:
        print(exercise.name)

    return render(request, 'index.html',
                  {'workoutPlan': workoutPlan, 'exercises': exercises, 'exercise_test': exercise_test, 'selected': selected})


# This function is not used anywhere
def importExercises(request):
    # Create the context that will be used when the button is clicked
    muscle = 'biceps'
    api_url = 'https://api.api-ninjas.com/v1/exercises?muscle={}'.format(muscle)
    response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY'})
    if response.status_code == requests.codes.ok:
        print(response.json('type'))
        print(response.text)
        exercise_data = response.json()
        exercise_type = exercise_data.get('type')

        print(f"Type: {exercise_type}")
    else:
        print("Error:", response.status_code, response.text)
    return render(request, 'index.html', {'responseText': response.text})

