# Generated by Django 4.2.7 on 2024-01-27 08:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_alter_books_upload_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='upload_date',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 1, 27, 8, 39, 42, 987187, tzinfo=datetime.timezone.utc)),
        ),
    ]