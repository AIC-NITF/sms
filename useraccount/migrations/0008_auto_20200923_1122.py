# Generated by Django 3.0.3 on 2020-09-23 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0007_auto_20200917_1247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='email',
        ),
        migrations.AddField(
            model_name='admin',
            name='email',
            field=models.EmailField(blank=True, max_length=60, null=True, verbose_name='email'),
        ),
        migrations.AddField(
            model_name='startup',
            name='email',
            field=models.EmailField(blank=True, max_length=60, null=True, verbose_name='email'),
        ),
    ]
