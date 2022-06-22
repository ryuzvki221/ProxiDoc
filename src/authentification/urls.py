from django.urls import path
from .views import login_view, register_view, error404_view, error500_view, logout_view, profile_view

urlpatterns = [
    path('login', login_view, name='login'),
    path('register', register_view, name='register'),
    path('page404', error404_view, name='error404'),
    path('page500', error500_view, name='error500'),
    path("logout", logout_view, name="logout"),
    path("profile", profile_view, name="profile"),
]
