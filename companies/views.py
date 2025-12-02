from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Company
from .forms import CompanyForm
from iamavailable.forms import JobForm
from iamavailable.models import Job, Application
from users.models import Profile

# Create your views here.
def companyDetail(request, id):
    company = get_object_or_404(Company, id=id)
    
    if request.user.is_authenticated:
        if company == request.user.profile.company:
            return redirect(reverse('my_company'))
    
    context = {
        'company': company,
        'jobs': Job.objects.filter(company__id=id)
    }
    
    return render(request, 'companies/detail.html', context)

@login_required(login_url='login')
def createCompany(request):
    if Company.objects.filter(owner=request.user.profile):
        return redirect(reverse('my_company'))
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('my_company'))
    else:
        form = CompanyForm()
    
    context = {
        'form': form
    }
    
    return render(request, 'companies/create_company.html', context)

@login_required(login_url='login')
def myCompany(request):    
    company = Company.objects.get(owner=request.user.profile)
    context = {
        'company': company,
        'jobs': Job.objects.filter(company__id=company.id)
    }
    
    return render(request, 'companies/company.html', context)

@login_required(login_url='login')
def editCompany(request):
    company = Company.objects.get(owner=request.user.profile)
    form = CompanyForm(instance=company)
    
    if request.method == "POST":
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
            return redirect(reverse('my_company'))
        
    context = { "form" : form }
    
    return render(request, 'companies/company_form.html', context)


@login_required(login_url='login')
def createJob(request):
    company = Company.objects.get(owner=request.user.profile)
    
    if company.owner != request.user.profile:
        return redirect(reverse('home'))
    
    if not Company.objects.filter(owner=request.user.profile):
        return redirect(reverse('create_company'))
    
    if request.method == 'POST':
        post_data = request.POST.copy()
        post_data['company'] = company
        form = JobForm(post_data)
        if form.is_valid():
            form.save()
            return redirect(reverse('my_company'))
    else:
        form = JobForm()   
    
    
    context = {
        "form": form,
        "company": company,
        "id": company.id
    }

    return render(request, 'companies/create_job.html',  context)

@login_required(login_url='login')
def editJob(request, id):
    job = Job.objects.get(id=id)
    
    if job.company != request.user.profile.company:
        return redirect('my_company')
    
    form = JobForm(instance=job)
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES, instance=job)
        if form.is_valid():
            form.save()
            return redirect(reverse('my_company'))
    
    context = {
        'form' : form,
        'job' : job
    }
    
    return render(request, 'companies/job_form.html', context)
    
    
@login_required(login_url='login')
def deleteJob(request, id):
    if request.method == 'DELETE':
        job = get_object_or_404(Job, id=id)
        job.delete()
        return JsonResponse({'message': 'deleted'}, status=204)

@login_required(login_url='login')
def getJob(request, id):
    
    print(request.user.profile.id)
    
    job = get_object_or_404(Job, id=id)
    applicants = Application.objects.filter(job=job)
    context = {
        'job': job,
        'applicants': applicants,
        'count': applicants.count()
    }
    
    return render(request, 'companies/job.html', context)

@login_required(login_url='login')
def getApplicant(request, id):
    applicant = get_object_or_404(Profile, id=id)
    application = get_object_or_404(Application, applicant=applicant)
    
    context = {
        'application': application,
    } 
    
    return render(request, 'companies/applicant.html', context)
    
