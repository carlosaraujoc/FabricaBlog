# Generated by Django 4.1.1 on 2022-09-17 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_monster_acoes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_monster',
            name='acoes',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='post_monster',
            name='caracteristicas',
            field=models.TextField(help_text='Perícias, Idiomas, Imunidades e Habilidades', max_length=200),
        ),
        migrations.AlterField(
            model_name='post_monster',
            name='descricao',
            field=models.TextField(max_length=100),
        ),
    ]