# Generated by Django 2.2.6 on 2019-11-01 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20191101_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='category',
            field=models.CharField(choices=[('1', 'All'), ('2', 'Medical'), ('3', 'Gumanytarian'), ('4', 'STEM')], default='', max_length=20, verbose_name='University category'),
        ),
    ]
