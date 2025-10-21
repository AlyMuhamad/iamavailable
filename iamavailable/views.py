from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Job, Tag
from .forms import JobForm

# Create your views here.

def index(request):
    search_query = ''
    location_query = ''
    
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    if request.GET.get('location_query'):
        location_query = request.GET.get('location_query')
      
    tags = Tag.objects.filter(name__icontains=search_query)
    
    context = {
        'jobs': Job.objects.distinct().filter(
            Q(title__icontains=search_query) | 
            Q(description__icontains=search_query) |
            Q(tags__in=tags) &
            Q(location__icontains=location_query)
            ),
        'search_query': search_query,
        'location_query': location_query
    }

    return render(request, 'iamavailable/index.html', context)

def job_detail(request, id):
    context = {
        'job': get_object_or_404(Job, id=id),
    }
    return render(request, 'iamavailable/detail.html', context)

@login_required(login_url='login')
def create_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    else:
        form = JobForm()   
    context = {
        "form": form
    }

    return render(request, 'iamavailable/create.html',  context)

# COMING FEEATURE
def update_job(request, id):
    job = Job.objects.get(id=id)
    form = JobForm(instance=job)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    else:
        form = JobForm()   
    context = {
        "form": form
    }

    # return render(request, 'iamavailable/create.html',  context)


def about(request):
    return render(request, 'iamavailable/about.html')
