from django.db import models
from users.models import Profile
import uuid

# Create your models here.
class Company(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    owner = models.OneToOneField(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    
    class Meta:
        verbose_name_plural = 'Companies'
    
    def __str__(self):
        return self.name

class Room(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    applicant = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"{self.company} | {self.applicant}"
    
class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.room} || {self.message}"
    
    class Meta:
        ordering = ['is_read', '-created']
