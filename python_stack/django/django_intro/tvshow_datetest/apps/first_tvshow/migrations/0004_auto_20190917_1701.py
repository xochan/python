# Generated by Django 2.1.7 on 2019-09-17 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_tvshow', '0003_auto_20190917_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='release_date',
            field=models.DateField(),
        ),
    ]
