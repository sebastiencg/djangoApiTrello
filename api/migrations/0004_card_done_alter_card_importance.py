# Generated by Django 5.0 on 2023-12-17 17:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_card_datetime_alter_list_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='done',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='card',
            name='importance',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MaxValueValidator(10)]),
        ),
    ]