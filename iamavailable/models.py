from django.db import models

from companies.models import Company
from users.models import Profile
import uuid
from django.utils import timesince
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class Job(models.Model):
    MODE_CHOICES = (
        ('Part-time', 'Part-time'),
        ('Full-time', 'Full-time')
    )
    
    MODEL_CHOICES = (
        ('Onsite', 'Onsite'),
        ('Hybrid', 'Hybrid'),
        ('Remote', 'Remote')
        )

    EXPERIENCE_CHOICES = (
        ('Intern', 'Intern'),
        ('Junior', 'Junior'),
        ('Senior', 'Senior'),
        ('Lead', 'Lead')
    )
    
    CATEGORY_CHOICES = (
        ('Uncategorized', 'Uncategorized'),
        ('Arts', 'Arts'),
        ('Business', 'Business'),
        ('Communications', 'Communications'),
        ('Education', 'Education'),
        ('Healthcare', 'Healthcare'),
        ('Hospitality', 'Hospitality'),
        ('Information technology', 'Information technology'),
        ('Law', 'Law'),
        ('Sales and Marketing', 'Sales and Marketing'),
        ('Science', 'Science'),
        ('Transportation', 'Transportation')
    )
    
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = CKEditor5Field('description', config_name='extends')
    experience = models.CharField(max_length=50, choices=EXPERIENCE_CHOICES, default='Junior')
    tags = models.ManyToManyField('Tag', blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Uncategorized')
    mode = models.CharField(max_length=50, choices=MODE_CHOICES, default='Full-time')
    model = models.CharField(max_length=50, choices=MODEL_CHOICES, default='Onsite')
    salary = models.PositiveBigIntegerField(blank=True, null=True)
    number = models.CharField(blank=True, null=True, max_length=11)
    email = models.EmailField(blank=True)

    def __str__(self):
        return f"{self.title} | {self.company}"
    
    @property
    def timesince(self):
        return timesince.timesince(self.created)
    
class Tag(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created']

class Saved(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.profile} | {self.job}"

class Application(models.Model):
    STATUS_CHOICES = (
        ('Undecided', 'Undecided'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected')
        )
    
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    applicant = models.ForeignKey(Profile,on_delete=models.CASCADE)
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    suitability = models.TextField()
    resume = models.URLField(max_length=300)
    expected_salary = models.PositiveBigIntegerField()
    notice = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Undecided')

    def __str__(self):
        return f"{self.job} | {self.applicant}"
    
    @property
    def timesince(self):
        return timesince.timesince(self.created)
    
class Subscription(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    
    def __str__(self):
        return self.email

class Contact(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    
    def __str__(self):
        return f"{self.name} | {self.email}"

class Notification(models.Model):
    TYPE_CHOICES = (
        ('Applicant', 'Applicant'),
        ('Company', 'Company'),
    )
    
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    applicant = models.ForeignKey(Profile,on_delete=models.CASCADE)
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    company = models.ForeignKey(Company,on_delete=models.CASCADE, blank=True, null=True)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='Undecided')
    read = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.job} | {self.applicant}"
    
    @property
    def timesince(self):
        return timesince.timesince(self.created)
