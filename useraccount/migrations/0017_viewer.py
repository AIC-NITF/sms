# Generated by Django 3.0.3 on 2021-04-30 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0016_account_is_viewer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Viewer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=60, null=True, verbose_name='email')),
                ('contact_no', models.CharField(blank=True, max_length=100, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]