from django.urls import path
from .views import index, job_detail, about, terms, contact, subscribe, faq

urlpatterns = [
    path('', index, name='home'),
    path('job/<str:id>/', job_detail, name='job_detail'),
    path('about/', about, name='about'),
    path('terms/', terms, name='terms'),
    path('faq/', faq, name='faq'),
    path('contact/', contact, name='contact'),
    path('subscribe/', subscribe, name='subscribe'),
]