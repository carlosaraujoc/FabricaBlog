from django.contrib import admin
from django.urls import path
from blog.views import behir, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('behir/', behir),
]
