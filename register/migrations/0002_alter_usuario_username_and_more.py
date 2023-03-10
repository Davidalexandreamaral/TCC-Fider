# Generated by Django 4.0.3 on 2022-05-01 14:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='username',
            field=models.CharField(max_length=25, unique=True, validators=[django.core.validators.RegexValidator(message='O tamanho do nome tem que ser entre 4 e 25', regex='^.{4,25}$'), django.core.validators.RegexValidator(message='O tamanho do nome tem que ser entre 4 e 25', regex='^.{4,25}$')], verbose_name='Nome de usuário'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='usernameinsensitive',
            field=models.CharField(max_length=25, unique=True, verbose_name='Nome de usuário'),
        ),
    ]
