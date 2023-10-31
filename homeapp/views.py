from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import WorkoutPlan, Exercises
import requests



# Create your views here.
def index(request):
    # Global variables
    selected = True
    print(selected)
    workoutPlan = WorkoutPlan.objects.all()
    exercises = Exercises.objects.all()
    print("ACTIVATED")

    # --- WORKOUT PLAN ---
    workout_plan = WorkoutPlan.objects.get(pk=4) #The primary key
    exercise_test = workout_plan.exercises.all()

    for exercise in exercise_test:
        print(exercise.name)

    #--- FULL BODY PLAN AND EXERCISES---
    full_body = WorkoutPlan.objects.filter(days=3)
    full_body_test = []
    for workout_plan in full_body:
        exercises_for_plan = workout_plan.exercises.all()
        full_body_test.extend(exercises_for_plan)

    # --- Find the full body variations ---
    full_body_var = WorkoutPlan.objects.filter(variation=1)
    full_body_var_info = []
    for workout_plan in full_body_var:
        exercises_for_variation = workout_plan.exercises.all()
        full_body_var_info.extend(exercises_for_variation)


    #--- Multi parameter ---
    multi_day_var = WorkoutPlan.objects.filter(variation=1).filter(days=3)
    multi_day_var_info = []
    for exercises_both in multi_day_var:
        exercises_for_both = exercises_both.exercises.all()
        multi_day_var_info.extend(exercises_for_both)

    return render(request, 'index.html',
                  {'workoutPlan': workoutPlan, 'exercises': exercises, 'exercise_test': exercise_test, 'selected': selected, 'full_body': full_body, 'full_body_test':full_body_test, 'full_body_var_info': full_body_var_info,'multi_day_var_info': multi_day_var_info })


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

