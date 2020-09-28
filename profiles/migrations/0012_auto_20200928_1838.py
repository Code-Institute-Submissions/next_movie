# Generated by Django 3.1 on 2020-09-28 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0011_auto_20200927_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='watched_movies_genres',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='watched_movies_years',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
    ]
