# Generated by Django 2.0.13 on 2019-07-02 17:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190702_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='eventdate',
            field=models.DateField(default=datetime.datetime(2019, 7, 2, 17, 32, 52, 382066, tzinfo=utc), verbose_name='Eventdate (YYYY-MM-DD)'),
        ),
    ]