from django.db import models
from django.contrib.auth.models import User
from shared_models.models import Book

class BookReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="reviews")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, related_name="reviews")
    review = models.TextField()
    reviewer_name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    star_rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return self.review[:50]