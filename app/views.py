from django.shortcuts import render
from django.contrib.auth.models import User

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
    dev = User.objects.get(username=username)
    return render(request, 'app/dev_profile.html')
