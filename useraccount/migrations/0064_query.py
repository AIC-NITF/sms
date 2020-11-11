# Generated by Django 3.0.3 on 2020-11-10 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0063_merge_20201110_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('about', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('message', models.CharField(blank=True, max_length=1000, null=True)),
                ('submitted_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='submitted date')),
            ],
        ),
    ]