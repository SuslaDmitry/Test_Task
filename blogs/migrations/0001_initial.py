# Generated by Django 3.0.8 on 2020-09-10 22:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=130)),
                ('text', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_edit', models.DateTimeField(auto_now_add=True)),
                ('date_publication', models.DateTimeField(auto_now_add=True)),
                ('public', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
    ]
