# Generated by Django 3.0.3 on 2020-10-19 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0031_auto_20201019_2132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workgenerator',
            old_name='forwared',
            new_name='forwarded',
        ),
    ]
