from django.shortcuts import render, redirect
from .models import Post_Monster
from .forms import create_monster


#Manager
def home(request):
    data = {}
    data['Monstros'] = Post_Monster.objects.all()
    return render(request, 'blog/home.html', data)


#Create
def create(request):
    data = {}
    form = create_monster(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    data['create'] = form
    return render(request, 'blog/form.html', data)


def update(request, pk):
    data = {}
    monstro = Post_Monster.objects.get(pk=pk)
    form = create_monster(request.POST or None, instance=monstro)
    if form.is_valid():
        form.save()
        return redirect('home')
    data['create'] = form
    data['monstro'] = monstro
    return render(request, 'blog/form.html', data)


def delete(request, pk):
    monstro = Post_Monster.objects.get(pk=pk)
    monstro.delete()
    return redirect('home')
