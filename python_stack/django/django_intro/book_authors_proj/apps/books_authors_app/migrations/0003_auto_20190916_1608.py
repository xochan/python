# Generated by Django 2.1.7 on 2019-09-16 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0002_book_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='notes',
        ),
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default='i love u all'),
            preserve_default=False,
        ),
    ]
