from email.policy import default
from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='moringa_graduates/profile_pics')
    work_title = models.CharField(max_length=1000, blank=True)
    professional_summary = models.TextField(blank=True)
    resume = models.FileField(upload_to='user_resumes/', null=True, blank=True)
    skills = models.TextField(blank=True)
    linkedin = models.CharField(max_length=5000, blank=True)
    github = models.CharField(max_length=5000, blank=True)
    twitter = models.CharField(max_length=5000, blank=True)
    portfolio = models.CharField(max_length=5000, blank=True)

    def __str__(self):
        return f"{self.user.username.title()}'s Profile"