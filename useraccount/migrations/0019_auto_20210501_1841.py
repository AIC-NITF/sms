# Generated by Django 3.0.3 on 2021-05-01 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0018_viewer_viewer_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='completed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='session',
            name='pm_am1',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='session',
            name='pm_am2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='session',
            name='time_out',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
