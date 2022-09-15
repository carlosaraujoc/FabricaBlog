from django.shortcuts import render


def home(request):
    return render(request, 'blog/home.html')

    
def behir(request):
    return render(request, 'blog/behir.html')