# Generated by Django 3.0.3 on 2020-10-07 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0019_auto_20201007_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='admin_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='startup',
            name='startup_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]