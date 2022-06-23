from django.db import models
from users.models import Profile


class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    course = models.CharField(max_length=5000, blank=True)
    institution = models.CharField(max_length=5000)
    from_date = models.DateField(blank=True)
    to_date = models.DateField(blank=True)

    def __str__(self):
        return f"{self.profile.user.username.title()}'s Educaiton History"



class Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    company = models.CharField(max_length=1000)
    from_date = models.DateField(blank=True)
    to_date = models.DateField(blank=True)
    responsibilities = models.TextField(blank=True)

    def __str__(self):
        return f"{self.profile.user.username.title()}'s Experience"