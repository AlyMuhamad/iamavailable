from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Job, Tag, Saved, Application
from .forms import JobForm, ApplicationForm
from datetime import date

# Create your views here.

def index(request):
    search_query = ''
    location_query = ''
    model_query = ''
    experience_query = ''
    
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    if request.GET.get('location_query'):
        location_query = request.GET.get('location_query')
    
    if request.GET.get('model_query'):
        model_query = request.GET.get('model_query')
    
    tags = Tag.objects.filter(name__icontains=search_query)
    
    jobs = Job.objects.distinct().filter(
            Q(title__icontains=search_query) | 
            Q(description__icontains=search_query) |
            Q(tags__in=tags) &
            Q(location__icontains=location_query) &
            Q(model__icontains=model_query) &
            Q(experience__icontains=experience_query) 
            )
    
    page = request.GET.get('page')
    results = 10
    paginator = Paginator(jobs, results)
    
    try:
        jobs = paginator.page(page)
    except PageNotAnInteger:
        page = 1 
        jobs = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        jobs = paginator.page(page)
    
    context = {
        'jobs': jobs,
        'search_query': search_query,
        'location_query': location_query,
        'model_query': model_query,
        'experience_query': experience_query,
        'paginator': paginator,
        'time': date
    }

    return render(request, 'iamavailable/index.html', context)

def job_detail(request, id):
    job = get_object_or_404(Job, id=id)
    
    saved = Saved.objects.filter(
        Q(profile=request.user.profile) &
        Q(job=job) 
    )
    
    applied = Application.objects.filter(
        Q(applicant=request.user.profile) &
        Q(job=job) 
    )

    if request.method == 'POST':
        post_data = request.POST.copy()
        post_data['job'] = job
        post_data['applicant'] = request.user.profile
        form = ApplicationForm(post_data)
        if form.is_valid():
            form.save()
            return redirect('job_detail', id=job.id)
            
    else:
        form = ApplicationForm()
        
    context = {
        'job': job,
        'saved': saved,
        'applied': applied,
        'form': form
    }
    
    return render(request, 'iamavailable/detail.html', context)

@login_required(login_url='login')
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

    return render(request, 'iamavailable/create.html',  context)


def about(request):
    return render(request, 'iamavailable/about.html')

def terms(request):
    return render(request, 'iamavailable/terms.html')

def contact(request):
    return render(request, 'iamavailable/contact.html')
