from django.shortcuts import render
from django.http import HttpResponse
from .models import WorkoutPlan

# Create your views here.
def index(request):
    workoutPlan = WorkoutPlan.objects.all()
    return render(request,'index.html', {'workoutPlan': workoutPlan})