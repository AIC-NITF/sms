# Generated by Django 3.0.3 on 2020-10-19 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0030_auto_20201019_1505'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forward',
            old_name='form_user',
            new_name='from_user',
        ),
        migrations.RenameField(
            model_name='reply',
            old_name='form_user',
            new_name='from_user',
        ),
        migrations.AddField(
            model_name='workgenerator',
            name='forwared',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='reply',
            name='to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='useraccount.WorkGenerator'),
        ),
    ]
