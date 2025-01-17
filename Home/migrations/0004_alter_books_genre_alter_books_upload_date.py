# Generated by Django 5.0 on 2023-12-08 09:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_books_author_books_genre_alter_books_upload_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='genre',
            field=models.CharField(choices=[('Poem', 'Poem'), ('Story', 'Story'), ('Artical', 'Artical'), ('Misc', 'Misc')], max_length=20),
        ),
        migrations.AlterField(
            model_name='books',
            name='upload_date',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 12, 8, 9, 55, 7, 401311, tzinfo=datetime.timezone.utc)),
        ),
    ]
