from django import forms
from .models import Job, Application, Contact
from companies.models import Company
from users.models import Profile 
from django_ckeditor_5.widgets import CKEditor5Widget

class JobForm(forms.ModelForm):
    company = forms.ModelChoiceField(queryset=Company.objects.all(), widget=forms.HiddenInput())
    class Meta:
        model = Job
        fields = ['title', 'location', 'company','description', 'experience', 'category','tags','salary', 'mode', 'model', 'number', 'email'] 
        widgets = {
            "description": CKEditor5Widget(attrs={"class": "django_ckeditor_5"}, config_name="custom"
            )
        }

class ApplicationForm(forms.ModelForm):
    job = forms.ModelChoiceField(queryset=Job.objects.all(), widget=forms.HiddenInput())
    applicant = forms.ModelChoiceField(queryset=Profile.objects.all(), widget=forms.HiddenInput())
    class Meta:
        model = Application
        fields = ['job', 'applicant' ,'suitability', 'resume', 'expected_salary', 'notice']
        labels = {
            'suitability': 'Why do you think you are the best candidate for this job?',
            'resume': 'Resume/CV link, Please upload your resume on Googledrive / Dropbox / Mediafire etc',
            'expected_salary': 'What is your expected salary?',
            'notice': 'What is your notice period?'
        }
        
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        labels = {
            'name': 'Your full-name',
            'email': 'Your email',
            'message': 'Your message'
        }