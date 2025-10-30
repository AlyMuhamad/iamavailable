from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Company
from .forms import CompanyForm
from iamavailable.models import Job

# Create your views here.
def company_detail(request, id):
    context = {
        'company': get_object_or_404(Company, id=id),
        'jobs': Job.objects.filter(company__id=id)
    }
    
    return render(request, 'companies/detail.html', context)

@login_required(login_url='login')
def create_company(request):
    if Company.objects.filter(owner=request.user.profile):
        return redirect(reverse('create_job'))
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('create_job'))
    else:
        form = CompanyForm()
    
    context = {
        'form': form
    }
    
    return render(request, 'companies/create.html', context)