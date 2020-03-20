# Generated by Django 3.0.3 on 2020-03-07 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('summary', models.TextField()),
                ('release_date', models.DateField()),
                ('rate', models.FloatField(default=0)),
            ],
        ),
    ]
