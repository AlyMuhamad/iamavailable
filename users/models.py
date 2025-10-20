from django.db import models
from django.contrib.auth.models import User
import uuid



# Create your models here.
class Profile(models.Model):
    TYPE_CHOICES = (
        ('Employee', 'Employee'),
        ('Employer', 'Employer')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default='profiles/default-profile.jpg')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='Employee')

    def __str__(self):
        return str(self.username)
    

