# Generated by Django 2.1.7 on 2019-09-24 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20190924_1100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follow',
            name='user',
        ),
        migrations.RemoveField(
            model_name='follow',
            name='user_fav_follow',
        ),
        migrations.RemoveField(
            model_name='friend',
            name='user',
        ),
        migrations.RemoveField(
            model_name='friend',
            name='user_fav_friend',
        ),
        migrations.RemoveField(
            model_name='like',
            name='post',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user_fav_like',
        ),
        migrations.DeleteModel(
            name='Follow',
        ),
        migrations.DeleteModel(
            name='Friend',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
