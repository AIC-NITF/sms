# Generated by Django 3.0.3 on 2020-11-01 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0060_auto_20201101_0054'),
    ]

    operations = [
        migrations.AddField(
            model_name='startup',
            name='founder_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
