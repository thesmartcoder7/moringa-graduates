"""
This file contains Django views for handling user-related functionalities, such as signup and profile update.

Functions:
    signup(request): Renders the signup page template and handles user registration.
    update(request): Renders the profile update page template and handles updating user information.

"""

from django.shortcuts import render, redirect
from users.forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def signup(request):
    """
    Renders the signup page template and handles user registration.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered signup page template.
    """
    form = SignupForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                f"Success! Please login to visit your account."
            )
            return redirect('users-signin')
        else:
            return render(request, 'users/signup.html', context)
    else:
        return render(request, 'users/signup.html', context)


@login_required
def update(request):
    """
    Renders the profile update page template and handles updating user information.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered profile update page template.
    """
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('app-dashboard')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/update.html', context)
