# Generated by Django 2.2.2 on 2019-09-20 11:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('trackerapp', '0003_auto_20190920_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 20, 11, 18, 21, 533702, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='projectusers',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 20, 11, 18, 21, 533702, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='projectversions',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 20, 11, 18, 21, 533702, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 20, 11, 18, 21, 533702, tzinfo=utc)),
        ),
    ]