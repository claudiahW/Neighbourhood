# Generated by Django 3.2.9 on 2022-01-05 04:59

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('neighs', '0003_profile_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
        migrations.AddField(
            model_name='neighborhood',
            name='neighs_image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='neighs_image'),
        ),
        migrations.AlterField(
            model_name='neighborhood',
            name='admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='contact',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
