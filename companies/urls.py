from django.urls import path
from .views import  company_detail

urlpatterns = [
    path('<str:id>/', company_detail, name='company_detail')
    # path('<str:id>/', company_detail, name='company_detail')
]
