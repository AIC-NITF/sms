# Generated by Django 3.0.3 on 2020-10-26 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0052_return_return_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='return',
            name='return_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='return date'),
        ),
    ]
