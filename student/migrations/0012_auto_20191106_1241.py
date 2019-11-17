# Generated by Django 2.2.6 on 2019-11-06 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0011_auto_20191105_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administration',
            name='adress',
            field=models.CharField(default='', max_length=1000, verbose_name='Administration adress'),
        ),
        migrations.AlterField(
            model_name='administration',
            name='name',
            field=models.CharField(default='', max_length=1000, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='teacher_lesson',
            field=models.CharField(default='', max_length=1000, verbose_name='Teacher lesson'),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='teacher_name',
            field=models.CharField(default='', max_length=1000, verbose_name='Teacher name'),
        ),
        migrations.AlterField(
            model_name='university',
            name='name',
            field=models.CharField(default='', max_length=1000, verbose_name='University name'),
        ),
        migrations.AlterField(
            model_name='university',
            name='region',
            field=models.CharField(default='', max_length=100, verbose_name='University region'),
        ),
    ]
