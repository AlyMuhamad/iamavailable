from django.db import models
import uuid

# Create your models here.
class Company(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.CharField()
    
    def __str__(self):
        return self.name