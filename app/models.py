"""
This file contains the Django model for the Project class.

The Project model represents a project created by a user in the application.
It contains various fields such as user, title, image, description, and link
to store information about the project.

Attributes:
    user (ForeignKey): A foreign key field representing the User who created the project.
    title (CharField): A character field to store the title of the project. It has a maximum length of 500 characters.
    image (ImageField): An image field to upload and store the project image. The images are stored in the 'moringa_graduates/project_images' directory.
    description (TextField): A text field to store the description of the project.
    link (CharField): A character field to store the link associated with the project. It has a maximum length of 2000 characters.

Methods:
    __str__(): Returns a string representation of the project title.

"""

from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='moringa_graduates/project_images')
    description = models.TextField()
    link = models.CharField(max_length=2000)

    def __str__(self):
        """
        Returns a string representation of the project title.

        Returns:
            str: The title of the project in title case.
        """
        return self.title.title()
