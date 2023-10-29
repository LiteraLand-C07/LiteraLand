from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    publisher = models.CharField(max_length=255)
    page_count = models.IntegerField()
    genre = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=13)
    language = models.CharField(max_length=255)
    published_date = models.DateField()

    def __str__(self):
        return self.title