# Generated by Django 4.0.5 on 2022-06-23 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='medium',
        ),
        migrations.AddField(
            model_name='profile',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='user_resumes/'),
        ),
    ]
