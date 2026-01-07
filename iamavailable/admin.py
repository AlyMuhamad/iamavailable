from django.contrib import admin
from .models import Job, Tag, Saved, Application, Subscription, Contact, Notification, Faq

# Register your models here.
admin.site.register(Job)
admin.site.register(Tag)
admin.site.register(Saved)
admin.site.register(Application)
admin.site.register(Subscription)
admin.site.register(Contact)
admin.site.register(Notification)
admin.site.register(Faq)