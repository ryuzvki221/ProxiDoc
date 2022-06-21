from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import login_view, register_view, error404_view, error500_view

urlpatterns = [
    path('login', login_view, name='login'),
    path('register', register_view, name='register'),
    path('page404', error404_view, name='error404'),
    path('page500', error500_view, name='error500'),
    path("logout", LogoutView.as_view(), name="logout")
]
