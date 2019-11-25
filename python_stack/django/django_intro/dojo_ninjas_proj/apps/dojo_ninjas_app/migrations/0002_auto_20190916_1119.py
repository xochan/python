# Generated by Django 2.1.7 on 2019-09-16 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.TextField(default='old dojo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ninja',
            name='dojo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ninjas', to='dojo_ninjas_app.Dojo'),
        ),
    ]
