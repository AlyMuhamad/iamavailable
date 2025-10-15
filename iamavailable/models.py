from django.db import models

# Create your models here.
class Jobs(models.Model):
    MODE_CHOICES = (
        ('part_time', 'Part-time'),
        ('full_time', 'Full-time')
    )
    
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    mode = models.CharField(max_length=50, choices=MODE_CHOICES, default='Full-time')
    company = models.CharField(max_length=100)
    salary = models.PositiveBigIntegerField()
    is_new = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} | {self.company}"