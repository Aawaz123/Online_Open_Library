# Generated by Django 5.0 on 2023-12-08 08:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='upload_date',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 12, 8, 8, 39, 40, 754387, tzinfo=datetime.timezone.utc)),
        ),
    ]
