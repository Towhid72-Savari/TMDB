# Generated by Django 3.0.2 on 2020-03-10 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_auto_20200310_0924'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='director',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
