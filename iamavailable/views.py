from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Job, Tag, Saved, Application, Subscription, Notification
from companies.models import Company
from .forms import ApplicationForm, ContactForm
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.core.mail import send_mail
from dotenv import load_dotenv
import os
import json

# Environment variables
load_dotenv()

# Global data
def notificationCount(request):
    if not request.user.is_authenticated:
        return {}
    
    applicant = request.user.profile
    try:
        company = Company.objects.get(owner=applicant)
        if company:
            notifications = Notification.objects.filter(
                Q(Q(company=company) & Q(type='Company') & Q(read=False)) |
                Q(Q(applicant=applicant) & Q(type='Applicant') & Q(read=False))
            )           
    except:
        notifications = Notification.objects.filter(applicant=applicant, type='Applicant', read=False)

    return {"notificationCount": notifications.count()}


# Create your views here.
def index(request):
    search_query = ''
    location_query = ''
    model_query = ''
    experience_query = ''
    date_query = datetime.now() - timedelta(days=1000)
    days = 0
    category_query = ''
    
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    if request.GET.get('location_query'):
        location_query = request.GET.get('location_query')
    
    if request.GET.get('model_query'):
        model_query = request.GET.get('model_query')
        
    if request.GET.get('experience_query'):
        experience_query = request.GET.get('experience_query')
    
    if request.GET.get('date_query'):
        days = request.GET.get('date_query')
        now = datetime.now()
        date_query = now - timedelta(days=int(days)) 
    
    if request.GET.get('category_query'):
        category_query = request.GET.get('category_query')
    
    tags = Tag.objects.filter(name__icontains=search_query)
    
    jobs = Job.objects.distinct().filter(
            (Q(title__icontains=search_query) | 
            Q(description__icontains=search_query) |
            Q(tags__in=tags)) &
            Q(location__icontains=location_query) &
            Q(model__icontains=model_query) &
            Q(experience__icontains=experience_query) &
            Q(created__gte=date_query) &
            Q(category__icontains=category_query) 
            ).order_by('-created')
    
    applications = ''
    if request.user.is_authenticated:
        applications = Application.objects.filter(applicant=request.user.profile)
    
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
        'category_query': category_query,
        'date_query': date_query,
        'days': days,
        'paginator': paginator,
        'applications': applications
    }

    return render(request, 'iamavailable/index.html', context)

def job_detail(request, id):
    job = get_object_or_404(Job, id=id)
    similar = Job.objects.filter(category=job.category).exclude(id=job.id)[0:3]
    
    if request.user.is_authenticated:
        authenticated = 1
        
        try:
            if job.company==request.user.profile.company:
                return redirect('get_job', id=job.id)
        except:
            pass
        
        saved = Saved.objects.filter(
            Q(profile=request.user.profile) &
            Q(job=job) 
        )
    
        applied = Application.objects.filter(
            Q(applicant=request.user.profile) &
            Q(job=job) 
        )
        
        applications = Application.objects.filter(applicant=request.user.profile)
        
    else:
        authenticated = 0
        saved = {}
        applied = {}
        applications = ''
    
    if request.method == 'POST':
        post_data = request.POST.copy()
        post_data['job'] = job
        post_data['applicant'] = request.user.profile
        form = ApplicationForm(post_data)
        if form.is_valid():
            form.save()
            
            Notification.objects.create(applicant=request.user.profile, job=job, company=job.company, type='Company')
            
            return redirect('job_detail', id=job.id)
            
    else:
        form = ApplicationForm()
        
    context = {
        'authenticated': authenticated,
        'job': job,
        'saved': saved,
        'applied': applied,
        'form': form,
        'similar': similar,
        'applications': applications
    }
    
    return render(request, 'iamavailable/detail.html', context)


def about(request):
    return render(request, 'iamavailable/about.html')

def terms(request):
    return render(request, 'iamavailable/terms.html')

def faq(request):
    return render(request, 'iamavailable/faq.html')

def contact(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('contact'))
    else:
        form = ContactForm()
    
    context = {
        'form': form
    }
    return render(request, 'iamavailable/contact.html', context)

def subscribe(request):    
    if request.method == 'POST':
        email = json.loads(request.body)['email']
        try:
            validate_email(email)
        except ValidationError as e:
            return JsonResponse({'message': 'Invalid email'}, status=400)
        else:
            if Subscription.objects.filter(email=email):
                return JsonResponse({'message': 'This email was used before'}, status=409)
            else:
                Subscription.objects.create(email=email)
                try:
                    subject = 'Welcome to IAmAvailable'
                    message = 'We are glad you are here '
                    send_mail(
                        subject,
                        message,
                        os.getenv('EMAIL_HOST_USER'),
                        [email],
                        fail_silently=False
                        )
                except e:
                    print(e)
    
                return JsonResponse({'message': 'Your email was subscribed'}, status=200)
                
        
