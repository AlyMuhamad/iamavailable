from django.db import models
from django.contrib.auth.models import User
import uuid



# Create your models here.
class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    linkedIn = models.URLField(max_length=300, blank=True, null=True)
    github = models.URLField(max_length=300, blank=True, null=True)
    portfolio = models.URLField(max_length=300, blank=True, null=True)
    
    def __str__(self):
        return str(self.username)
