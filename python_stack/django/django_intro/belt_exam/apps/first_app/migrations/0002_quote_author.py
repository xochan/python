# Generated by Django 2.1.7 on 2019-09-20 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='author',
            field=models.CharField(default='superman', max_length=100),
            preserve_default=False,
        ),
    ]