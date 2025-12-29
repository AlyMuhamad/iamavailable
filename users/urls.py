from django.urls import path
from django.contrib.auth import views as auth_views
from users.views import loginUser, logoutUser, registerUser, userAccount, editAccount, saved, notification, chat, singleChat, saveJob, applications, singleApplication, personalInfo

urlpatterns = [
    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('signup/', registerUser, name='signup'),
    
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='reset_password.html'),
         name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='reset_password_sent.html'),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='reset.html'),
         name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='reset_password_complete.html'),
         name="password_reset_complete"),
    
    path('', userAccount, name='account'),
    path('personal-info/', personalInfo, name='personal-info'),
    path('personail-info/edit', editAccount, name='edit-account'),
    path('saved/', saved, name='saved'),
    path('notification/', notification, name='notification'),
    path('chat/', chat, name='chat'),
    path('applications/', applications, name='applications'),
    path('application/<str:id>/', singleApplication, name='singleApplication'),
    path('chat/<str:id>/', singleChat, name='single-chat'),
    path('save/<str:id>/', saveJob, name='save-job')
]