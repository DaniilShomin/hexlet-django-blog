from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse

def index(request):
        url = reverse('article', kwargs={"tags":'python', "article_id":42})
        return redirect(url)

def about(request):
    return render(request, "about.html")
