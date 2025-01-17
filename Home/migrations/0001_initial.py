# Generated by Django 5.0 on 2023-12-08 07:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_icon', models.ImageField(upload_to='book_icon/')),
                ('book_name', models.CharField(max_length=50)),
                ('book_description', models.TextField(blank=True, null=True)),
                ('book_file', models.FileField(upload_to='book_file/')),
                ('upload_date', models.DateField(blank=True, default=datetime.datetime(2023, 12, 8, 7, 6, 57, 146153, tzinfo=datetime.timezone.utc))),
            ],
        ),
    ]
