# Generated by Django 3.2.4 on 2022-05-17 14:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saints_website', '0020_alter_calendar_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='month',
            field=models.CharField(default=datetime.datetime(2022, 5, 17, 14, 9, 50, 94910), max_length=50),
        ),
    ]