from django import forms
from app.models import *


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = [
            'course', 
            'institution',
            'from_date',
            'to_date'
        ]


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = [
            'company',
            'from_date',
            'to_date',
            'responsibilities'
        ]
    