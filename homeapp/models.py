from django.db import models

# Create your models here.
class WorkoutPlan(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    difficulty = models.IntegerField()

    def __str__(self):
        return self.name