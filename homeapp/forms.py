from django import forms
from .models import WorkoutPlan, Exercises, RadioBtn

class TaskForm(forms.ModelForm):
    class Meta:
        # model = RadioBtn
        # fields = ['day_radio_field']
        #
        # day_radio_field = forms.ChoiceField(
        #     widget=forms.RadioSelect,
        #     choices=RadioBtn.Choices,
        # )

        model = WorkoutPlan
        fields = ['name', 'days', 'variation']

