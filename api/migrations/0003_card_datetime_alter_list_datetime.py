# Generated by Django 5.0 on 2023-12-17 15:59

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_board_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='list',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
