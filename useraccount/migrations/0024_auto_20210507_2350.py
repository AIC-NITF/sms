# Generated by Django 3.0.3 on 2021-05-07 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0023_submissionideanest'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_ideanest_check',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='is_ideanest_viewer',
            field=models.BooleanField(default=False),
        ),
    ]
