from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'app/index.html')



def developers(request):
    return render(request, 'app/developers.html')