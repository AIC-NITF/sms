# Generated by Django 3.0.3 on 2020-10-19 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0033_remove_workgenerator_forwarded'),
    ]

    operations = [
        migrations.AddField(
            model_name='workgenerator',
            name='forward',
            field=models.BooleanField(default=False),
        ),
    ]
