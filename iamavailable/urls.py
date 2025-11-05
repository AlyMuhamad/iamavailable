from django.urls import path
from .views import index, job_detail, about

urlpatterns = [
    path('', index, name='home'),
    path('job/<str:id>/', job_detail, name='job_detail'),
    path('about/', about, name='about'),
]