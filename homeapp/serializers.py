from rest_framework import serializers
from .models import WorkoutPlan, Exercises, UserCreatedEx


class WorkoutPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutPlan
        fields = '__all__'


class ExercisesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercises
        fields = '__all__'


class UserCreatedExSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCreatedEx
        fields = '__all__'
