from django.shortcuts import redirect
from django.shortcuts import render


# Create login view
def login(request):
    return render(request, 'auth/login.html')


# Create register view
def register(request):
    return redirect('/')


# Create error 404 view
def error404(request):
    return render(request, 'auth/404.html')
