# Generated by Django 3.0.2 on 2020-03-12 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_auto_20200310_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='rate_counter',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
