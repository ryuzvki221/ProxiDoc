from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegisterForm


# Create login view
def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid Credentials'
        else:
            msg = 'Error validating the form'
    return render(request, 'auth/account/login.html', {"form": form, "msg": msg})


# Create register view
def register_view(request):
    msg = None
    success = False

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/auth/login/">login</a>'
            success = True
            # return redirect ("/auth/login/")
        else:
            msg = 'Form is not valid'
    else:
        form = RegisterForm()

    return render(request, "auth/account/register.html", {'form': form, "msg": msg, "success": success})


# Create error 404 view
def error404_view(request):
    return render(request, 'auth/404.html')
