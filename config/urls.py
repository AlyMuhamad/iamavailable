from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('iamavailable.urls')),
    path('account/', include('users.urls')),
    path('company/', include('companies.urls')),
]
