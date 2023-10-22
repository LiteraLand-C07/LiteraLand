from django.shortcuts import render
from shared_models.models import Book
from bookcollections.models import BookCollection, StatusBaca
from django.http import HttpResponseRedirect,HttpResponse, HttpResponseNotFound
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Avg
import json

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

def get_collection_json(request,id):
    book = Book.objects.get(pk=id)
    book_collection = BookCollection.objects.filter(book=book)
    return HttpResponse(serializers.serialize('json', book_collection))

@csrf_exempt
def add_collection(request,id):
    if request.method == 'POST':
        book_data = Book.objects.get(pk=id)
        rating = request.POST.get('rating')
        current_page = request.POST.get('current_page')
        status_baca = request.POST.get('status_baca')

        new_collection = BookCollection(book=book_data,rating=rating,current_page=current_page,status_baca=status_baca)
        new_collection.save()

        return HttpResponse(b"CREATED", status=201)
    
    return HttpResponseNotFound()

@csrf_exempt
def edit_collection(request,id):
    if request.method == 'POST':
        bookCollection = BookCollection.objects.get(pk=id)
        rating = request.POST.get('rating')
        current_page = request.POST.get('current_page')
        status_baca = request.POST.get('status_baca')

        bookCollection.rating = rating
        bookCollection.current_page = current_page
        bookCollection.status_baca = status_baca
        bookCollection.save()

        return HttpResponse(b"EDITED", status=201)
    
    return HttpResponseNotFound() 

def show_collections(request):
    book_collections = BookCollection.objects.all()
    context = {
        'book_collections':book_collections,
        'StatusBaca':StatusBaca,
    }

    return render(request,'collections.html',context)