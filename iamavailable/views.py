from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Job
from .forms import JobForm

# Create your views here.

def index(request):
    context = {
        'jobs': Job.objects.all(),
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
