from django.urls import path
from .views import  companyDetail, createCompany, myCompany, editCompany, editJob

urlpatterns = [
    path('create-company/', createCompany, name='create_company'),
    path('my-company/', myCompany, name='my_company'),
    path('edit-company/', editCompany, name='edit_company'),
    path('edit-job/', editJob, name='edit_job'),
    path('<str:id>/', companyDetail, name='company_detail')
]
