# Generated by Django 3.1 on 2020-09-12 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0013_auto_20200912_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='submission_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
