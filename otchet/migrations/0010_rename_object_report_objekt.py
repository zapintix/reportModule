# Generated by Django 4.2.13 on 2024-06-14 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('otchet', '0009_remove_useraut_user_remove_report_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='object',
            new_name='objekt',
        ),
    ]
