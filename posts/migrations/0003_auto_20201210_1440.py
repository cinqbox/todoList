# Generated by Django 3.1.4 on 2020-12-10 05:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('posts', '0002_auto_20201210_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='Urgency',
            field=models.BooleanField(default=True, verbose_name='緊急度'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 10, 5, 40, 31, 219447, tzinfo=utc),
                                       verbose_name='作成日時'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 13, 5, 40, 31, 219447, tzinfo=utc),
                                       verbose_name='締切'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='importance',
            field=models.BooleanField(default=True, verbose_name='重要度'),
        ),
    ]
