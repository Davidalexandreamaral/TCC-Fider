# Generated by Django 4.0.3 on 2022-05-01 14:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_alter_usuario_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='username',
            field=models.CharField(max_length=25, unique=True, validators=[django.core.validators.RegexValidator(message='O tamanho do nome tem que ser entre 4 e 25', regex='^.{4,25}$'), django.core.validators.RegexValidator(message='Somente caracteres alfanuméricos são permitidos.', regex='^[a-zA-Z0-9]*$')], verbose_name='Nome de usuário'),
        ),
    ]