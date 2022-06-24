from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name='app-home'),
    path('developers/', views.developers, name='app-developers'),
    path('profile/<username>', views.dev_profile, name='app-profile'),
    path('dashboard/', views.dashboard, name='app-dashboard'),
    path('new_project/', views.add_project, name='app-add-project'),
    path('search/', views.search, name='app-search')
]
