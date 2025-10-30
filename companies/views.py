from django.shortcuts import render, get_object_or_404
from .models import Company
from iamavailable.models import Job

# Create your views here.
def company_detail(request, id):
    context = {
        'company': get_object_or_404(Company, id=id),
        'jobs': Job.objects.filter(company__id=id)
    }
    
    return render(request, 'companies/detail.html', context)