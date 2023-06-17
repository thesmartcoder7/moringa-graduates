"""
This file contains the Django form for the ProjectForm class.

The ProjectForm is a ModelForm that is used to create or update Project instances.
It specifies the fields and validation rules for creating or updating a Project object.

Attributes:
    Meta (class): The Meta inner class defines metadata for the form, such as the model it is associated with and the fields to include.

Methods:
    None

"""

from django import forms
from app.models import *


class ProjectForm(forms.ModelForm):
    class Meta:
        """
        Metadata for the ProjectForm class.

        Attributes:
            model (Model): The model class associated with the form (Project).
            fields (list): The fields from the model that should be included in the form (title, image, description, link).

        """
        model = Project
        fields = [
            'title',
            'image',
            'description',
            'link'
        ]
