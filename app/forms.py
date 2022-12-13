from django import forms
from app.models import *


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'title',
            'image',
            'description',
            'link'
        ]