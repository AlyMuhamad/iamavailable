from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Profile
import os
from dotenv import load_dotenv

# Environment variables
load_dotenv()

# To create a user profile automatically when user signs up
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username = user.username,
            email = user.email,
            name = user.first_name
        )
        
        
        subject = 'Welcome to IAmAvailable'
        html_message = render_to_string('email.html', {
            'username': user.username
        })
        
        message = strip_tags(html_message)
        
        send_mail(
            subject,
            message,
            os.getenv('EMAIL_HOST_USER'),
            [profile.email],
            html_message=html_message,
            fail_silently=False
        )

post_save.connect(createProfile, sender=User)


# To delete a user when the his profile is deleted
def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()

post_delete.connect(deleteUser, sender=Profile)

# To update a user when the profile is updated
def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()
    
    
post_save.connect(updateUser, sender=Profile)