
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def student_login(request):

    error = None

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('dashboard')

        else:
            error = "Invalid username or password"

    return render(request, 'Students/login.html', {
        'error': error
    })


@login_required
def dashboard(request):
    return render(request, 'Students/dashboard.html')


def student_logout(request):
    logout(request)
    return redirect('login')
