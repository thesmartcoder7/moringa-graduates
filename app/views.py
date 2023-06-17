"""
This file contains Django views for handling different HTTP requests and rendering templates.

Functions:
    home(request): Renders the home page template.
    developers(request): Renders the developers page template and displays a list of all developers.
    dev_profile(request, username): Renders the developer profile page template for a specific user.
    dashboard(request): Renders the dashboard page template for the authenticated user.
    add_project(request): Renders the add project page template and handles the creation of a new project.
    search(request): Handles the search functionality and renders the search page template.

"""

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from app.models import Project
from django.contrib.auth.decorators import login_required
from app.forms import *


def home(request):
    """
    Renders the home page template.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered home page template.
    """
    return render(request, 'app/index.html')


def developers(request):
    """
    Renders the developers page template and displays a list of all developers.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered developers page template.
    """
    all_devs = User.objects.all()
    context = {
        'all_devs': all_devs
    }
    return render(request, 'app/developers.html', context)


def dev_profile(request, username):
    """
    Renders the developer profile page template for a specific user.

    Args:
        request (HttpRequest): The HTTP request object.
        username (str): The username of the user whose profile is being accessed.

    Returns:
        HttpResponse: The HTTP response object containing the rendered developer profile page template.
    """
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
    """
    Renders the dashboard page template for the authenticated user.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered dashboard page template.
    """
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
    """
    Renders the add project page template and handles the creation of a new project.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered add project page template.
    """
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


def search(request):
    """
    Handles the search functionality and renders the search page template.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered search page template.
    """
    if request.method == 'POST':
        all_users = User.objects.all()
        filtered_users = []
        search_term = request.POST['search'].split(' ')
        for user in all_users:
            for term in search_term:
                if term.lower() in user.username.lower() and user not in filtered_users and term != "" \
                    or term.lower() in user.first_name.lower() and user not in filtered_users and term != "" \
                    or term.lower() in user.last_name.lower() and user not in filtered_users and term != "" \
                    or term.lower() in user.profile.skills.lower() and user not in filtered_users and term != "":
                    filtered_users.append(user)

    return render(request, 'app/search.html', {'all_devs': filtered_users})
