from django.shortcuts import render
from shared_models.models import Book
from bookcollections.models import BookCollection, StatusBaca
from django.db.models import Avg

# Create your views here.
def show_detail_buku(request,id):
    book = Book.objects.get(pk=id)
    average_rating = BookCollection.objects.filter(book=book).aggregate(Avg('rating'))['rating__avg']

    context = {
        'book':book,
        'rating':average_rating,
        'StatusBaca':StatusBaca,
        'range':range(1,11),
    }

    return render(request,'detail_buku.html',context)