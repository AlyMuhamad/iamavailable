from django.db import models

# Create your models here.
class Jobs(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100, default='')
    description = models.TextField()
    company = models.CharField(max_length=100)
    salary = models.PositiveBigIntegerField()
    is_new = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} | {self.company}"