# Generated by Django 4.0.3 on 2022-05-01 17:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0007_alter_tweet_tweetauthor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]