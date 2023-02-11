from django.db import models

# Create your models here.


def upload_news_image(instance, filename):
    return f'images/{instance.name}/{filename}'


class Movie(models.Model):

    name = models.CharField(max_length=155)
    description = models.TextField(null=True, blank=True)
    duration = models.FloatField()
    rate = models.FloatField()
    year = models.FloatField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to=upload_news_image, blank=True)
    is_published = models.BooleanField(default=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'



