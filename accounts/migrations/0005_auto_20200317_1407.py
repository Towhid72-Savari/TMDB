# Generated by Django 3.0.2 on 2020-03-17 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200317_1344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='watch_list',
        ),
        migrations.DeleteModel(
            name='UserWatchList',
        ),
    ]
