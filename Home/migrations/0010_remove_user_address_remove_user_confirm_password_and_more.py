# Generated by Django 4.2.7 on 2024-01-27 17:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0009_alter_books_upload_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='confirm_password',
        ),
        migrations.AlterField(
            model_name='books',
            name='upload_date',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 1, 27, 17, 50, 58, 969500, tzinfo=datetime.timezone.utc)),
        ),
    ]
