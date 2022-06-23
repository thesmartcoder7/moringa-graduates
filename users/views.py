from django.shortcuts import render, redirect
from users.forms import *
from django.contrib import messages

# Create your views here.
def signup(request):
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
                f"Success! Please login to visit your accout."
            )
            return redirect('users-signin')
        else:
            return render(request, 'users/signup.html', context)
    else:
        return render(request, 'users/signup.html', context)