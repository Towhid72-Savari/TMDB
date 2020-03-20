from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib import auth
from movies.models import Movies
from django.conf import settings


# Create your models here.
class User(auth.models.User, PermissionsMixin):
    watch_list = models.ManyToManyField(Movies, blank=True)

    def __str__(self):
        return f'{self.username}'


class UserWatchList(models.Model):
    movie_added_to_list = models.ForeignKey(Movies, on_delete=models.CASCADE,
                                            related_name='movie_on_list')
    user_who_add_to_list = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_added', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user_who_add_to_list) + ' - ' + str(self.movie_added_to_list)
