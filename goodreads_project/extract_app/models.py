from django.db import models


# Create your models here.

class Book(models.Model):
    # Define a model for Book objects

    # Title of the book (required)
    title = models.CharField(null=False, blank=False, max_length=100)

    # Author of the book
    author = models.CharField(max_length=100)

    # Year the book was published
    published_year = models.IntegerField()

    # Rating of the book
    rating = models.FloatField()

    # Edition of the book (optional)
    # edition = models.IntegerField()

    # String representation of the Book object (title)
    def __str__(self):
        return self.title
