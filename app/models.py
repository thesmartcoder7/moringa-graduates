from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='moringa_graduates/project_images')
    description = models.TextField()
    link = models.CharField(max_length=2000)

    def __str__(self):
        return self.title.title()