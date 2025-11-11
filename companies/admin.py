from django.contrib import admin
from .models import Company, Room, Message

# Register your models here.
admin.site.register(Company)
admin.site.register(Room)
admin.site.register(Message)