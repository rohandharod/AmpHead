# Generated by Django 3.1.2 on 2020-12-08 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_channel'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='genre',
            field=models.CharField(default='', max_length=100000),
        ),
    ]
