from django.db import models
from shared_models.models import Book
from django.contrib.auth.models import User

# Create your models here.
class ListBook(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    access = models.CharField(max_length=100, choices=[('public', 'Public'),
        ('private', 'Private')
    ], default='public')
    description = models.TextField()
    books = models.ManyToManyField(Book, blank=True, related_name='list_books')
    cover_image = models.ImageField(upload_to='list_book_covers/', blank=True, null=True)

    def __str__(self):
        return self.name

