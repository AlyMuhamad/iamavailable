from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello world from the deepest point I have reached')