# Generated by Django 3.2.6 on 2021-12-06 01:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bullseyeapp', '0002_auto_20211021_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlystats',
            name='month',
            field=models.DateField(default=datetime.date(2021, 12, 1)),
        ),
    ]