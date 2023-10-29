from django.db import models


# Create your models here.
# class WorkoutPlan(models.Model):
#     name = models.CharField(max_length=255)
#     type = models.CharField(max_length=255)
#     difficulty = models.IntegerField()
#
#     def __str__(self):
#         return self.name


# class MuscleGroup(models.Model):
#     name = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.name
#

class Exercises(models.Model):
    name = models.CharField(max_length=255)
    muscle_group = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    #muscleGroup = models.ManyToManyField(MuscleGroup)
    # difficulty = models.IntegerField()

    # This just renames what is listed in the database
    def __str__(self):
        return self.name


class WorkoutPlan(models.Model):
    name = models.CharField(max_length=255)
    split = models.CharField(max_length=100)
    days = models.CharField(max_length=100)
    exercises = models.ManyToManyField(Exercises)

    def __str__(self):
        return self.name
