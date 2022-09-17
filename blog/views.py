from django.shortcuts import render
from .models import Post_Monster


def home(request):
    data = {}
    data['Monstros'] = Post_Monster.objects.all()
    return render(request, 'blog/home.html', data)


def create(request):
    return render(request, 'blog/')


def post(request):
    return render(request, 'blog/')


def update(request):
    return render(request, 'blog/')


def delete(request):
    return render(request, 'blog/')
