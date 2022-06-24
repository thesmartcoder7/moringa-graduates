from django.shortcuts import render
from django.contrib.auth.models import User
from app.models import Project
from django.contrib.auth.decorators import login_required



# Create your views here.
def home(request):
    return render(request, 'app/index.html')



def developers(request):
    all_devs = User.objects.all()
    context = {
        'all_devs': all_devs
    }
    return render(request, 'app/developers.html', context)



def dev_profile(request, username):
    user = User.objects.get(username=username)
    user_skills = user.profile.skills.split()
    user_projects = Project.objects.filter(user=user)
    context = {
        'dev': user,
        'skills': user_skills,
        'projects': user_projects
    }
    return render(request, 'app/dev_profile.html', context)



@login_required
def dashboard(request):
    user = User.objects.get(username=request.user.username)
    user_skills = user.profile.skills.split()
    user_projects = Project.objects.filter(user=user)
    context = {
        'dev': user,
        'skills': user_skills,
        'projects': user_projects
    }
    return render(request, 'app/dashboard.html', context)
