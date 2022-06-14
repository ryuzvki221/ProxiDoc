from django.shortcuts import redirect
from django.shortcuts import render

# Create login view
def login(request):
    return render(request, 'auth/login.html')


# Create register view
def register(request):
    return redirect('/')


# Create account view
def account(request):
    return redirect('/')


# Create logout view
def logout(request):
    return redirect('/')
