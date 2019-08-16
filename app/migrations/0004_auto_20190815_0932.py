# Generated by Django 2.2.3 on 2019-08-15 04:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190815_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='region_name',
            field=models.CharField(max_length=500, unique=True),
        ),
        migrations.AlterField(
            model_name='regionmodel',
            name='time',
            field=models.TimeField(default=datetime.time(9, 32, 39, 309241)),
        ),
    ]
