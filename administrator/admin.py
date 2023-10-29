from django.contrib import admin
from shared_models.models import Book
from administrator.models import BookQueue

# Register your models here.
admin.site.register(Book)
admin.site.register(BookQueue)