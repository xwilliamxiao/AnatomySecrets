from django.contrib import admin
from .models import WorkoutPlan, Exercises

# Register your models here.
admin.site.register(WorkoutPlan)
admin.site.register(Exercises)

