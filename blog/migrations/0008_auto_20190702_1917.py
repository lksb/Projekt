# Generated by Django 2.0.13 on 2019-07-02 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190702_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='eventdate',
            field=models.DateField(blank=True, verbose_name='Eventdate (DD.MM.YYYY)'),
        ),
    ]