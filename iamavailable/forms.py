from django import forms
from .models import Jobs


class JobForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = ['title', 'location', 'description', 'salary', 'company', 'mode'] 
