# Generated by Django 3.0.8 on 2020-09-11 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_blogpost_date_publication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='date_publication',
            field=models.DateTimeField(),
        ),
    ]