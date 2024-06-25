from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=50)
    director = models.CharField(max_length=20)
    release_date = models.DateField()
    genre = models.CharField(max_length=50)
    description = models.TextField()
    poster_image = models.ImageField(upload_to='posters/', blank=True, null=True)

    def __str__(self):
        return self.title

