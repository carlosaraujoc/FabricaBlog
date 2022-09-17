from urllib import request
from django.forms import ModelForm
from .models import Post_Monster


class create_monster (ModelForm):
    class Meta:
        model = Post_Monster
        fields = ['nome', 'tendencia', 'dificuldade', 'STR', 'DEX', 'CON', 'INT',
        'WIS', 'CHA', 'caracteristicas',' acoes', 'descricao']