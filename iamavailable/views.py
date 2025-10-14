from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    context = {
        'first_name': 'Aly',
        'last_name': 'Mohamed',
        'movies': ['500 days of summer', 'whiplash', 'gladiator']
    }

    return render(request, 'iamavailable/index.html', context)

def about(request):
    return render(request, 'iamavailable/about.html')

def hello(request, first_name):
    return HttpResponse(f"Hello {first_name}")