# Generated by Django 3.0.3 on 2020-10-30 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0058_blogpost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='from_user',
        ),
    ]