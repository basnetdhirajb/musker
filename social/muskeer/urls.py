from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('profiles/', views.profiles, name = 'profiles'),
    path('profile/<int:pk>', views.profile, name = 'profile'),
]