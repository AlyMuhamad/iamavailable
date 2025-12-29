from django import forms
from .models import Company


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'location', 'description', 'website', 'linkedIn', 'email', 'size']
        labels = {
            'size': 'Employees count'
        }
