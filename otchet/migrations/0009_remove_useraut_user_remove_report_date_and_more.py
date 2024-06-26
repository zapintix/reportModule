# Generated by Django 4.2.13 on 2024-06-13 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otchet', '0008_remove_report_user_aut_report_refresh_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraut',
            name='user',
        ),
        migrations.RemoveField(
            model_name='report',
            name='date',
        ),
        migrations.RemoveField(
            model_name='report',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='report',
            name='refresh_token',
        ),
        migrations.RemoveField(
            model_name='report',
            name='type',
        ),
        migrations.AddField(
            model_name='report',
            name='assortment',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='image_id',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='user_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='report',
            name='department',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='report',
            name='object',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='report',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='Object',
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
        migrations.DeleteModel(
            name='Type',
        ),
        migrations.DeleteModel(
            name='UserAut',
        ),
    ]
