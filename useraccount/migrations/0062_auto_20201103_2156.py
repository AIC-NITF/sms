# Generated by Django 3.0.3 on 2020-11-03 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0061_startup_founder_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitorsheet',
            name='date_of_filling',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='date of filling'),
        ),
    ]
