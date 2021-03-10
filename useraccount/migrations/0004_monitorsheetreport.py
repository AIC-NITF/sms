# Generated by Django 3.0.3 on 2021-01-14 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0003_delete_tractionsheet'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonitorSheetReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ips_till_date', models.CharField(blank=True, max_length=100, null=True)),
                ('recognisation_till_date', models.CharField(blank=True, max_length=100, null=True)),
                ('funds_till_date', models.CharField(blank=True, max_length=100, null=True)),
                ('jobs_created_till_date', models.CharField(blank=True, max_length=100, null=True)),
                ('sales_till_date', models.CharField(blank=True, max_length=100, null=True)),
                ('revenew_till_date', models.CharField(blank=True, max_length=100, null=True)),
                ('expendicture_till_date', models.CharField(blank=True, max_length=100, null=True)),
                ('ips_last_month', models.CharField(blank=True, max_length=100, null=True)),
                ('recognisation_last_month', models.CharField(blank=True, max_length=100, null=True)),
                ('funds_last_month', models.CharField(blank=True, max_length=100, null=True)),
                ('jobs_created_last_month', models.CharField(blank=True, max_length=100, null=True)),
                ('sales_last_month', models.CharField(blank=True, max_length=100, null=True)),
                ('revenew_last_month', models.CharField(blank=True, max_length=100, null=True)),
                ('expendicture_last_month', models.CharField(blank=True, max_length=100, null=True)),
                ('problems', models.CharField(blank=True, max_length=2000, null=True)),
                ('oppertunities', models.CharField(blank=True, max_length=2000, null=True)),
                ('out_reach', models.CharField(blank=True, max_length=2000, null=True)),
                ('intervention', models.CharField(blank=True, max_length=2000, null=True)),
                ('partnership_mou', models.CharField(blank=True, max_length=1000, null=True)),
                ('monitor_meeting', models.CharField(blank=True, max_length=1000, null=True)),
                ('action_plan', models.CharField(blank=True, max_length=2000, null=True)),
                ('help_required', models.CharField(blank=True, max_length=2000, null=True)),
                ('first_atempt', models.BooleanField(default=True)),
                ('allow_edit', models.BooleanField(default=False)),
                ('date_of_filling', models.DateTimeField(auto_now_add=True, verbose_name='report date_of_filling')),
                ('connect_startup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='useraccount.StartUp')),
            ],
        ),
    ]