from django import forms
from .models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'location', 'company','description', 'experience','tags','salary', 'mode', 'model', 'number', 'email'] 