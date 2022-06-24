from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from app.models import Project
from django.contrib.auth.decorators import login_required
from app.forms import *



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



@login_required
def add_project(request):
    add_form = ProjectForm()
    context = { 
        'add_form': add_form,
    }
    user = User.objects.get(username=request.user.username)
    if request.method == 'POST':
        add_form = ProjectForm(request.POST, request.FILES,)
        if add_form.is_valid():
            project = Project.objects.create(
                user=user, 
                image=request.FILES.get('image'), 
                title=request.POST.get('title'), 
                link=request.POST.get('link'), 
                description=request.POST.get('description')
            )
            project.save()
            return redirect('app-dashboard')
        else:
            add_form = ProjectForm(request.POST)
            return render(request, 'app/add_project.html', context)
    
    return render(request, 'app/add_project.html', context)
