from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    title = 'Django project'
    return render(
        request,
        'articles/index.html',
        context={
            'title': title,
        },
    )
