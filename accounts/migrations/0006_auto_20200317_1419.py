# Generated by Django 3.0.2 on 2020-03-17 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0013_comment'),
        ('accounts', '0005_auto_20200317_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='watch_list',
            field=models.ManyToManyField(blank=True, to='movies.Movies'),
        ),
        migrations.CreateModel(
            name='UserWatchList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_added_to_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_on_list', to='movies.Movies')),
                ('user_who_add_to_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_list', to='accounts.User')),
            ],
        ),
    ]