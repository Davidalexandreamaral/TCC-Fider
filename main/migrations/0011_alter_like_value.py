# Generated by Django 4.0.3 on 2022-05-01 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_like_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='value',
            field=models.IntegerField(blank=True, choices=[('Like', 'Like'), ('Unlike', 'Unlike')], max_length=8),
        ),
    ]