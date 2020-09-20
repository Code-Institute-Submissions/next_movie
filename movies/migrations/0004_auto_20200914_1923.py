# Generated by Django 3.1 on 2020-09-14 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_movie_ratings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='imdb_rating',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True),
        ),
    ]