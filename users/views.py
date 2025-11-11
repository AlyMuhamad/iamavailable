from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, ProfileForm
from .models import Profile
from companies.models import Company, Room, Message

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
            
            return redirect('edit-account')
        
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
    profile = request.user.profile
    context = {
        'profile': profile,
        'profile_img': profile.profile_image.url
    }
    return render(request, 'users/account.html', context)


@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        
        if form.is_valid():
            form.save()
            return redirect('account')
    
    context = { 'form': form } 
    return render(request, 'users/account_form.html', context)


@login_required(login_url='login')
def saved(request):
    
    return render (request, 'users/saved.html')


@login_required(login_url='login')
def notification(request):
    
    return render (request, 'users/notification.html')


@login_required(login_url='login')
def chat(request):
    rooms , companyAccount = getChats(request)
    
    context = {
        'rooms': rooms,
        'companyAccount': companyAccount
    }
    
    return render (request, 'users/chat.html', context)

@login_required(login_url='login')
def singleChat(request, id):
    
    if request.method == 'POST':
        print(request)
    
    rooms , companyAccount = getChats(request)
    room = get_object_or_404(Room, id=id)
    msgs = Message.objects.filter(room=room)
    
    context = {
        'rooms': rooms,
        'companyAccount': companyAccount,
        'room': room,
        'id': room.id,
        'msgs': msgs
    }
    
    return render(request, 'users/single_chat.html', context)


# Helper functions
def getChats(request):
    profile = request.user.profile
    company = Company.objects.filter(owner=profile)
    if company:
        rooms = Room.objects.filter(company__in=company)
        companyAccount = True
    else:
        rooms = Room.objects.filter(applicant=profile)
        companyAccount = False
    
    return rooms, companyAccount