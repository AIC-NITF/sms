# Generated by Django 3.0.3 on 2020-10-10 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0021_startup_allow_edit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='startup',
            name='allow_edit',
        ),
        migrations.AddField(
            model_name='monitorsheet',
            name='allow_edit',
            field=models.BooleanField(default=False),
        ),
    ]