from django.db import models
from shared_models.models import Book

# Create your models here.
class StatusBaca(models.TextChoices):
    COMPLETED = 'C', 'Completed'
    CURRENTLY_READING = 'R', 'Reading'
    PLAN_TO_READ = 'PR', 'Plan to Read'
    DROPPED = 'D','Dropped'

class BookCollection(models.Model):
    CHOICES = [(i,i) for i in range(11)]
    book = models.ForeignKey(Book,on_delete=models.CASCADE,null=True)
    rating = models.IntegerField(choices=CHOICES)
    current_page = models.IntegerField()
    status_baca = models.CharField(
        max_length=2,
        choices=StatusBaca.choices,
        default=StatusBaca.PLAN_TO_READ,
    )