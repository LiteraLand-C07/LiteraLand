from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BookQueue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    publisher = models.CharField(max_length=255)
    page_count = models.IntegerField()
    genre = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=13)
    language = models.CharField(max_length=255)
    published_date = models.DateField()

