# Generated by Django 2.2.3 on 2019-07-29 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nexiiapp', '0009_remove_upload_system_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactionhistory',
            name='download_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='transactionhistory',
            name='download_filename',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transactionhistory',
            name='download_token',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='upload',
            name='system_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
