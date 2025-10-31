from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Company
from .forms import CompanyForm
from iamavailable.forms import JobForm
from iamavailable.models import Job

# Create your views here.
def companyDetail(request, id):
    context = {
        'company': get_object_or_404(Company, id=id),
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
    
    return render(request, 'companies/create.html', context)

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
def editJob(request, id):
    job = Job.objects.get(id=id)
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
    