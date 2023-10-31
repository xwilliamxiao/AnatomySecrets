from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import WorkoutPlan, Exercises
from .forms import TaskForm
from django.views.decorators.http import require_POST
import requests


# Create your views here.
def index(request):
    # Fetch form from Forms
    form = TaskForm()

    # Global variables
    selected = True
    print(selected)
    workoutPlan = WorkoutPlan.objects.all()
    exercises = Exercises.objects.all()
    print("ACTIVATED")

    # --- WORKOUT PLAN ---
    workout_plan = WorkoutPlan.objects.get(pk=4)  # The primary key
    exercise_test = workout_plan.exercises.all()

    for exercise in exercise_test:
        print(exercise.name)

    # --- FULL BODY PLAN AND EXERCISES---
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

    # --- Multi parameter ---
    multi_day_var = WorkoutPlan.objects.filter(variation=1).filter(days=3)
    multi_day_var_info = []
    for exercises_both in multi_day_var:
        exercises_for_both = exercises_both.exercises.all()
        multi_day_var_info.extend(exercises_for_both)

    # makingWork = 0
    # # --- Trying to make the submit button work
    # if request.method == 'POST' and 'search' in request.POST:
    #     selected_radio_btn = request.POST.get('workoutDays')
    #     if selected_radio_btn == 'threeDays':
    #         #Give the user a random three day a week workout
    #         print("Now we are talking my friends...")
    #     print("HELLO ITS WORKINGT :)")
    #     makingWork = makingWork + 1



    # GOOD STUFF

    if request.method == "POST":
        workout_plan_day = request.POST.get('workoutDays')  # gets the radio button value
        #search_workouts = WorkoutPlan.objects.filter(days=workout_plan_day) #checks if the 'days' column has anything related to the radio button selected

        # I want to print out each exercise for the workoutplans
        workout_var = request.POST.get('workoutVar')
        #search_var = WorkoutPlan.objects.filter(variation=workout_var)

        #search both
        search_both = WorkoutPlan.objects.filter(days=workout_plan_day).filter(variation=workout_var)

        #Want to just print the exercises in the workout now
        exercise_info = []


        return render(request, 'index.html',
                      {'workoutPlan': workoutPlan, 'exercises': exercises, 'exercise_test': exercise_test,
                       'selected': selected, 'full_body': full_body,
                       'full_body_test': full_body_test, 'full_body_var_info': full_body_var_info,
                       'multi_day_var_info': multi_day_var_info,
                       'form': form, 'search_both': search_both})

    return render(request, 'index.html',
                  {'workoutPlan': workoutPlan, 'exercises': exercises, 'exercise_test': exercise_test,
                   'selected': selected, 'full_body': full_body,
                   'full_body_test': full_body_test, 'full_body_var_info': full_body_var_info,
                   'multi_day_var_info': multi_day_var_info,
                   'form': form, })


@require_POST
def create_task(request):
    form = TaskForm(request.POST)  # The request.POST just feeds the whole body with the information

    if form.is_valid():
        form.save()  # taking the task object and saving it
        return redirect('index')

    # return HttpResponse('Received request')


# @require_POST
# def choose_plan(request):
#     # --- Trying to make the submit button work\
#
#     if request.method == 'POST':
#         day = request.POST.get('name')
#
#         selected_radio_btn = request.POST.get('workoutDays')
#         if selected_radio_btn == 'threeDays':
#             # Give the user a random three day a week workout
#             print("Now we are talking my friends...")
#         elif selected_radio_btn == 'fourDays':
#             # Give the user a random three day a week workout
#             print("---------------")
#             # --- Multi parameter ---
#             multi_day_var = WorkoutPlan.objects.filter(variation=1).filter(days=3)
#             multi_day_var_info = []
#             for exercises_both in multi_day_var:
#                 exercises_for_both = exercises_both.exercises.all()
#                 multi_day_var_info.extend(exercises_for_both)
#
#         print("HELLO ITS WORKINGT :)")
#         return redirect('index')

    # @require_POST
    # def choose_plan(request):
    #     # --- Trying to make the submit button work\
    #
    #     if request.method == 'POST' and 'search' in request.POST:
    #         selected_radio_btn = request.POST.get('workoutDays')
    #         if selected_radio_btn == 'threeDays':
    #             # Give the user a random three day a week workout
    #             print("Now we are talking my friends...")
    #         elif selected_radio_btn == 'fourDays':
    #             # Give the user a random three day a week workout
    #             print("---------------")
    #             # --- Multi parameter ---
    #             multi_day_var = WorkoutPlan.objects.filter(variation=1).filter(days=3)
    #             multi_day_var_info = []
    #             for exercises_both in multi_day_var:
    #                 exercises_for_both = exercises_both.exercises.all()
    #                 multi_day_var_info.extend(exercises_for_both)
    #
    #         print("HELLO ITS WORKINGT :)")
    #         return redirect('index')
