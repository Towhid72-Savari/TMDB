from django.contrib import admin
from movies.models import Movies, ActorMovie, UserRater, Comment

# Register your models here.
admin.site.register(Movies)
admin.site.register(ActorMovie)
admin.site.register(UserRater)
admin.site.register(Comment)
