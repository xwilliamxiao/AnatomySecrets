from django.db import models


# Create your models here.
class Exercises(models.Model):
    name = models.CharField(max_length=255)
    muscle_group = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    # This just renames what is listed in the database
    def __str__(self):
        return self.name


class WorkoutPlan(models.Model):
    name = models.CharField(max_length=255)
    split = models.CharField(max_length=100)
    days = models.CharField(max_length=100)
    variation = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=100)
    exercises = models.ManyToManyField(Exercises, related_name='workout_plans')

    # This just renames what is listed in the database
    def __str__(self):
        return self.name
