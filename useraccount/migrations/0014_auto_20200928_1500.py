# Generated by Django 3.0.3 on 2020-09-28 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0013_startup_legal_entity_register'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OurTeamMembers',
            new_name='TeamMembers',
        ),
    ]