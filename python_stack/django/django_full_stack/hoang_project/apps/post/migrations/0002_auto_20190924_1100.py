# Generated by Django 2.1.7 on 2019-09-24 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20190924_1100'),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user_favorite',
        ),
        migrations.AddField(
            model_name='post',
            name='user_fav_post',
            field=models.ManyToManyField(related_name='fav_post', to='login.User'),
        ),
    ]
