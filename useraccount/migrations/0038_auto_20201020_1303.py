# Generated by Django 3.0.3 on 2020-10-20 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0037_auto_20201020_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forward',
            name='forwared_work',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
