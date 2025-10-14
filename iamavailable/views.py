from django.shortcuts import render, get_object_or_404
from .models import Jobs

# Create your views here.

def index(request):
    context = {
        'jobs': Jobs.objects.all(),
    }
    return render(request, 'iamavailable/index.html', context)

def job_detail(request, pk):
    context = {
        'job': get_object_or_404(Jobs, pk=pk),
    }
    return render(request, 'iamavailable/detail.html', context)


def about(request):
    return render(request, 'iamavailable/about.html')
