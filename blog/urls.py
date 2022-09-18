from django.urls import path
from .views import delete, home, create, update, delete


urlpatterns = [
    path('', home, name='home'),
    path('create/', create, name='new_monster'),
    path('update/<int:pk>/', update, name='update_monster'),
    path('delete/<int:pk>/', delete, name='delete_monster'),
]
