# Generated by Django 4.0.3 on 2022-05-01 17:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_replays_like'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Replays',
            new_name='Replys',
        ),
    ]