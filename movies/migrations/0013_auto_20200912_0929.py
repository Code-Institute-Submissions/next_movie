# Generated by Django 3.1 on 2020-09-12 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0012_auto_20200910_2054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='submission_date',
        ),
        migrations.AlterField(
            model_name='review',
            name='author_rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
