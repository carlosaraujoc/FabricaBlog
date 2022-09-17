from django.shortcuts import render, redirect
from .models import Post_Monster
from .forms import create_monster


def home(request):
    data = {}
    data['Monstros'] = Post_Monster.objects.all()
    return render(request, 'blog/home.html', data)


def create(request):
    data = {}
    form = create_monster(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    data['create'] = form
    return render(request, 'blog/form.html', data)



'''def post(request):
    return render(request, 'blog/', data)


def update(request):
    return render(request, 'blog/', data)


def delete(request):
    return render(request, 'blog/', data)'''
