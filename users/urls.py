from django.urls import path
from users.views import loginUser, logoutUser, registerUser, userAccount, editAccount, saved, notification, chat

urlpatterns = [
    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('signup/', registerUser, name='signup'),
    path('account/', userAccount, name='account'),
    path('edit-account/', editAccount, name='edit-account'),
    path('saved/', saved, name='saved'),
    path('notification/', notification, name='notification'),
    path('chat/', chat, name='chat')
]