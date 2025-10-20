from django.db import models
from users.models import Profile
import uuid


# Create your models here.
class Job(models.Model):
    MODE_CHOICES = (
        ('Part-time', 'Part-time'),
        ('Full-time', 'Full-time')
    )

    EXPERIENCE_CHOICES = (
        ('Intern', 'Intern'),
        ('Junior', 'Junior'),
        ('Senior', 'Senior'),
        ('Lead', 'Lead')
    )
    owner = models.ForeignKey(Profile, null=True, blank=True,on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    experience = models.CharField(max_length=50, choices=EXPERIENCE_CHOICES, default='Junior')
    tags = models.ManyToManyField('Tag', blank=True)
    mode = models.CharField(max_length=50, choices=MODE_CHOICES, default='Full-time')
    company = models.CharField(max_length=100)
    salary = models.PositiveBigIntegerField()
    number = models.CharField(blank=True, null=True, max_length=11)
    email = models.EmailField(blank=True)
    is_new = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} | {self.company}"
    
class Tag(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
