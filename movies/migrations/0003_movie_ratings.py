# Generated by Django 3.1 on 2020-09-13 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_watched_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='ratings',
            field=models.JSONField(default=None, null=True),
        ),
    ]