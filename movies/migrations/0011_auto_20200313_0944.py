# Generated by Django 3.0.2 on 2020-03-13 06:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0010_movies_rate_counter'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_rated', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rated', to='movies.Movies')),
                ('user_rater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rates', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='movies',
            name='rater',
            field=models.ManyToManyField(blank=True, null=True, through='movies.UserRater', to=settings.AUTH_USER_MODEL),
        ),
    ]
