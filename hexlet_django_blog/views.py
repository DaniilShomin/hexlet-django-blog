from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse

def index(request):
        return render(request, "index.html")

def about(request):
    return render(request, "about.html")
