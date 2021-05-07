# Generated by Django 3.0.3 on 2021-04-29 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0013_session_submission_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='sanvriddhi',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sanvriddhi',
            name='comp_identification_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sanvriddhi',
            name='dspp_registered',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='sanvriddhi',
            name='founder_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='sanvriddhi',
            name='founders_designation',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='sanvriddhi',
            name='gov_program',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sanvriddhi',
            name='inubatee_level',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sanvriddhi',
            name='legal_entity',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sanvriddhi',
            name='legal_entity_register',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sanvriddhi',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sanvriddhi',
            name='msme_registered',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='sanvriddhi',
            name='operational_model',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sanvriddhi',
            name='sector',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sanvriddhi',
            name='start_date_incubation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sanvriddhi',
            name='startup_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='sanvriddhi',
            name='startup_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sanvriddhi',
            name='team_head',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sanvriddhi',
            name='team_members',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sanvriddhi',
            name='type_of_incubatee',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='sanvriddhi',
            name='website',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sanvriddhi',
            name='women_led_startup',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]