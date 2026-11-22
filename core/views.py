from django.shortcuts import render

def home(request):

    context = {
        'name': 'Lary',
        'course': 'Django'
    }

    return render(request, 'core/home.html', context)


def about(request):

    return render(request, 'core/about.html')