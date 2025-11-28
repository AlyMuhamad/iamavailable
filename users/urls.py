from django.urls import path
from django.contrib.auth import views as auth_views
from users.views import loginUser, logoutUser, registerUser, userAccount, editAccount, saved, notification, chat, singleChat, saveJob

urlpatterns = [
    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('signup/', registerUser, name='signup'),
    
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    path('', userAccount, name='account'),
    path('edit-account/', editAccount, name='edit-account'),
    path('saved/', saved, name='saved'),
    path('notification/', notification, name='notification'),
    path('chat/', chat, name='chat'),
    path('chat/<str:id>/', singleChat, name='single-chat'),
    path('save/<str:id>/', saveJob, name='save-job')
]