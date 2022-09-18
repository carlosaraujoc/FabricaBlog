from django.forms import ModelForm
from .models import Post_Monster


class create_monster (ModelForm):
    class Meta:
        model = Post_Monster
        fields = ['nome', 'tendencia', 'dificuldade', 'caracteristicas', 'acoes', 'descricao', 'STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
