from django.urls import path
from .views import index, job_detail, about, create_job

urlpatterns = [
    path('', index, name='home'),
    path('job/<int:pk>/', job_detail, name='job_detail'),
    path('about/', about, name='about'),
    path('create-job/', create_job, name='create_job'),
]