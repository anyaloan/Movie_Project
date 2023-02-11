from django.db import models
from movie.models import upload_news_image

# Create your models here.

class Actor(models.Model):

    name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)
    description = models.TextField(null=True, blank=True)
    average_movie_rate = models.FloatField()
    date_of_birth = models.DateField()
    image = models.ImageField(upload_to=upload_news_image, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Actor'
        verbose_name_plural = 'Actors'
