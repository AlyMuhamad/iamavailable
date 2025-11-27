from django.db import models

from companies.models import Company
from users.models import Profile
import uuid
from django.utils import timesince


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
    
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    experience = models.CharField(max_length=50, choices=EXPERIENCE_CHOICES, default='Junior')
    tags = models.ManyToManyField('Tag', blank=True)
    mode = models.CharField(max_length=50, choices=MODE_CHOICES, default='Full-time')
    model = models.CharField(max_length=50, choices=MODEL_CHOICES, default='Onsite')
    salary = models.PositiveBigIntegerField()
    number = models.CharField(blank=True, null=True, max_length=11)
    email = models.EmailField(blank=True)
    is_new = models.BooleanField(default=False)

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
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    applicant = models.ForeignKey(Profile,on_delete=models.CASCADE)
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    suitability = models.TextField()
    resume = models.URLField(max_length=300)
    expected_salary = models.PositiveBigIntegerField()
    
    
    def __str__(self):
        return f"{self.job} | {self.applicant}"