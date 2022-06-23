from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name='app-home'),
    path('developers/', views.developers, name='app-developers'),
    path('profile/<username>', views.dev_profile, name='app-profile')
]
