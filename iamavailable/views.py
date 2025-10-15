from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Jobs
from .forms import JobForm

# Create your views here.

def index(request):
    jobs = Jobs.objects.all()

    context = {
        'jobs': jobs,
    }

    print(jobs)

    return render(request, 'iamavailable/index.html', context)

def job_detail(request, pk):
    context = {
        'job': get_object_or_404(Jobs, pk=pk),
    }
    return render(request, 'iamavailable/detail.html', context)


def create_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            # Save the data
            form.save()
            return redirect(reverse('home'))
    else:
        form = JobForm()
        
    context = {
        "form": form
    }

    return render(request, 'iamavailable/create.html',  context)

def about(request):
    return render(request, 'iamavailable/about.html')
