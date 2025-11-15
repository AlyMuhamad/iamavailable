from django.urls import path
from users.views import loginUser, logoutUser, registerUser, userAccount, editAccount, saved, notification, chat, singleChat, saveJob

urlpatterns = [
    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('signup/', registerUser, name='signup'),
    path('', userAccount, name='account'),
    path('edit-account/', editAccount, name='edit-account'),
    path('saved/', saved, name='saved'),
    path('notification/', notification, name='notification'),
    path('chat/', chat, name='chat'),
    path('chat/<str:id>/', singleChat, name='single-chat'),
    path('save/<str:id>/', saveJob, name='save-job')
]