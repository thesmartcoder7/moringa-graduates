# Generated by Django 4.0.5 on 2022-06-23 08:05

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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_title', models.CharField(blank=True, max_length=1000)),
                ('professional_summary', models.TextField(blank=True)),
                ('skills', models.TextField(blank=True)),
                ('linkedin', models.CharField(blank=True, max_length=5000)),
                ('github', models.CharField(blank=True, max_length=5000)),
                ('twitter', models.CharField(blank=True, max_length=5000)),
                ('medium', models.CharField(blank=True, max_length=5000)),
                ('portfolio', models.CharField(blank=True, max_length=5000)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
