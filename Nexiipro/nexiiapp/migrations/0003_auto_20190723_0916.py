# Generated by Django 2.2.3 on 2019-07-23 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nexiiapp', '0002_auto_20190722_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercredit',
            name='download_credit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
        migrations.AddField(
            model_name='usercredit',
            name='upload_credit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
    ]
