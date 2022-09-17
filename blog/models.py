from django.db import models

tendencias = (
    ('LG', 'Leal e Bom'),
    ('NG', 'Neutro e Bom'),
    ('CG', 'Caótico e Bom'),
    ('LN', 'Leal e Neutro'),
    ('NN', 'Neutro e Neutro'),
    ('CN', 'Caótico e Neutro'),
    ('LE', 'Leal e Mau'),
    ('NE', 'Neutro e Mau'),
    ('CE', 'Caótico e Mau'),
)


class Post_Monster(models.Model):
    nome = models.CharField(max_length=50)
    tendencia = models.CharField(choices=tendencias, max_length=20)
    dificuldade = models.IntegerField()
    STR = models.IntegerField()
    DEX = models.IntegerField()
    CON = models.IntegerField()
    INT = models.IntegerField()
    WIS = models.IntegerField()
    CHA = models.IntegerField()
    caracteristicas = models.TextField(
        max_length=200, help_text="Perícias, Idiomas, Imunidades...")
    acoes = models.TextField()
    descricao = models.TextField()

    def __str__(self):
        return self.nome
