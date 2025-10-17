from django.db import models
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()

# Create your models here.
class Job(models.Model):
    MODE_CHOICES = (
        ('Part-time', 'Part-time'),
        ('Full-time', 'Full-time')
    )
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_jobs')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
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
