from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm

# Create your views here.
def registerUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            
            messages.success(request, 'User account was created')
            
            login(request, user)
            
            return redirect('home')
        
        else:
            messages.error(request, 'Something went wrong, Please try again')
            
    
    context = {
        'form': CustomUserCreationForm
    }

    return render(request, 'users/signup.html', context) 


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password is incorrect')

    return render(request, 'users/login.html') 


def logoutUser(request):
    logout(request)
    messages.error(request, 'User was successfully logout')
    return redirect('login')


@login_required(login_url='login')
def userAccount(request):
    context = {
        'profile': request.user.profile
    }
    return render(request, 'users/account.html', context)