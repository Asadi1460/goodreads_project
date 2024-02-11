from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(null=False, blank=False, max_length=100)
    author = models.CharField(max_length=100)
    published_year = models.IntegerField()
    rating = models.FloatField()
    # edition = models.IntegerField()

    def __str__(self):
        return self.title

