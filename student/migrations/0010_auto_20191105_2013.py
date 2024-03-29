# Generated by Django 2.2.6 on 2019-11-05 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0009_remove_university_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='administration',
            name='owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='owner2', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='teachers',
            name='owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='owner1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='university',
            name='about',
            field=models.TextField(default='', verbose_name='About University'),
        ),
    ]
