from django.db import models
from django.contrib.auth.models import User
from actress.models import Actor
from django.utils import timezone


# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=256)
    summary = models.TextField()
    release_date = models.DateField()
    rate = models.FloatField(default=0)
    cast_list = models.ManyToManyField(Actor, through='ActorMovie')
    icon = models.ImageField(upload_to='images/', null=True)
    image = models.ImageField(upload_to='images/', null=True)
    genre = models.CharField(max_length=256)
    director = models.CharField(max_length=256)
    rate_counter = models.PositiveIntegerField(default=1)
    rater = models.ManyToManyField(User, through='UserRater', null=True, blank=True)

    def summary_card_body(self):
        return self.summary[:70] + '...'

    def __str__(self):
        return self.title

    def cast_list_func(self):
        movies_actors = Actor.objects.filter(actors_movies__movie_id=self.pk)
        return movies_actors

    def comment_func(self):
        return self.comments.filter(movie_id=self.pk)


class ActorMovie(models.Model):
    movie = models.ForeignKey(Movies, related_name='casts', on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, related_name='actors_movies', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.actor) + ' - ' + str(self.movie)


class UserRater(models.Model):
    user_rater = models.ForeignKey(User, related_name='rates', on_delete=models.CASCADE)
    movie_rated = models.ForeignKey(Movies, related_name='rated', on_delete=models.CASCADE)
    user_rate = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.user_rater) + ' - ' + str(self.movie_rated)


class Comment(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cm_author')
    cm_text = models.TextField()
    cm_date = models.DateTimeField(default=timezone.now)