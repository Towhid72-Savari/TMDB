# Generated by Django 3.0.2 on 2020-03-09 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20200309_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='release_date',
            field=models.DateField(unique_for_date=False, unique_for_month=False),
        ),
    ]