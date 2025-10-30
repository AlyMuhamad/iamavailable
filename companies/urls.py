from django.urls import path
from .views import  company_detail, create_company

urlpatterns = [
    path('create-company/', create_company, name='create_company'),
    path('<str:id>/', company_detail, name='company_detail')
]
