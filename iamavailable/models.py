from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Jobs(models.Model):
    MODE_CHOICES = (
        ('Part-time', 'Part-time'),
        ('Full-time', 'Full-time')
    )
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_jobs')
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    mode = models.CharField(max_length=50, choices=MODE_CHOICES, default='Full-time')
    company = models.CharField(max_length=100)
    salary = models.PositiveBigIntegerField()
    number = models.CharField(blank=True, null=True, max_length=11)
    email = models.EmailField(blank=True)
    is_new = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} | {self.company}"