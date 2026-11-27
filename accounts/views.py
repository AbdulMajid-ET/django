from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            request.session['username'] = username

            return redirect('dashboard')

        else:
            return render(request, 'accounts/login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'accounts/login.html')


@login_required
def dashboard(request):

    username = request.session.get('username')

    return render(request, 'accounts/dashboard.html', {
        'username': username
    })  

def user_logout(request):

    if request.method == 'POST':
        logout(request)

        return redirect('login')

    return redirect('dashboard')
