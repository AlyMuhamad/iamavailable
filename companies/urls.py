from django.urls import path
from .views import  companyDetail, createCompany, myCompany, editCompany, editJob, createJob, deleteJob, getJob, getApplicant

urlpatterns = [
    path('create-company/', createCompany, name='create_company'),
    path('my-company/', myCompany, name='my_company'),
    path('my-company/', myCompany, name='my_company'),
    path('edit-company/', editCompany, name='edit_company'),
    path('create-job/', createJob, name='create_job'),
    path('job/<str:id>/', getJob, name='get_job'),
    path('user/<str:id>/', getApplicant, name='get_applicant'),
    path('edit-job/<str:id>/', editJob, name='edit_job'),
    path('delete-job/<str:id>/', deleteJob, name='delete_job'),
    path('<str:id>/', companyDetail, name='company_detail')
]
