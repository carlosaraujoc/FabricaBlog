# Generated by Django 4.1.1 on 2022-09-17 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_monster_acoes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_monster',
            name='acoes',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post_monster',
            name='descricao',
            field=models.TextField(),
        ),
    ]
