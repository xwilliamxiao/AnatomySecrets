from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import WorkoutPlan, Exercises, UserCreatedEx
from django.views.decorators.http import require_POST
import requests
from .serializers import WorkoutPlanSerializer, ExercisesSerializer, UserCreatedExSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


# Create your views here.
class WorkoutPlanList(APIView):
    def get(self, request):
        workoutPlan = WorkoutPlan.objects.all()
        # --- Testing out serializing the workoutplan for the front end ---
        data = WorkoutPlanSerializer(workoutPlan, many=True).data
        print(data)
        # --- End of serializing ---

        return Response(data)

    # This is only going to be used for the User Created Workout Plans
    # EVERYTHING ELSE DOES NOT NEED IT INCLUDING THIS ONE RN (WorkoutPlan) ITS AN EXAMPLE
    def post(self, request):
        serializer = WorkoutPlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response('Bad Data', status=status.HTTP_400_BAD_REQUEST)


class ExercisesList(APIView):
    def get(self, request):
        exercisesList = Exercises.objects.all()
        # --- Testing out serializing the workoutplan for the front end ---
        data = ExercisesSerializer(exercisesList, many=True).data
        print(data)
        # --- End of serializing ---

        return Response(data)


class UserCreatedExList(APIView):
    def get(self, request):
        userCreatedExList = UserCreatedEx.objects.all()
        # --- Testing out serializing the workoutplan for the front end ---
        data = UserCreatedExSerializer(userCreatedExList, many=True).data
        print(data)
        # --- End of serializing ---

        return Response(data)

    def post(self, request):
        serializer = UserCreatedExSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response('Bad Data', status=status.HTTP_400_BAD_REQUEST)


# ------------------------ OLD BACKEND -----------------------------------------
def index(request):
    workoutPlan = WorkoutPlan.objects.all()

    # --- Testing out serializing the workoutplan for the front end ---
    data = WorkoutPlanSerializer(workoutPlan, many=True).data
    print(data)
    # --- End of serializing ---

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
        new_exercise = UserCreatedEx.objects.create(exercise_name=new_name, muscle_group=new_muscle_group,
                                                    exercise_description=new_description)
        return redirect('create')
    user_exercise = UserCreatedEx.objects.all()
    return render(request, 'create.html', {'user_exercise': user_exercise})
