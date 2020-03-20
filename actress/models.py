from django.db import models
from django.utils import timezone


# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=256)
    born_date = models.DateField()
    icon = models.ImageField(upload_to='images/')
    biography = models.TextField(null=True)

    def get_age(self):
        return timezone.now().year - self.born_date.year

    def brief_summary(self):
        return self.biography[:300] + '...'

    def __str__(self):
        return self.name
